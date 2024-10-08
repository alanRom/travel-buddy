import os
from typing import List
import requests
import praw


from api_utils.types.reddit_subreddit_search_response import RedditSubredditSearchResult, SubredditSearchChild
from api_utils.utils import get_separate_location_parts
from api_utils.types.reddit_subreddit_restricted_search import PostChild, RedditSubredditRestrictedSearch
from api_utils.types.general import LocationType
from api_utils.types.google_nearby_search_result import GoogleNearbySearch
from .api_keys import google_geocode_base_endpoint, google_key, google_nearby_search_endpoint, ipinfo_base_endpoint,ipinfo_key, reddit_base_endpoint, reddit_client_key, reddit_secret_key
from .types.google_geocoding_responses import SampleGoogleGeocodingResponse
from .types.ipinfo_response import SampleIpinfoResponse
import json
from difflib import SequenceMatcher

reddit = praw.Reddit(
    client_id=reddit_client_key,
    client_secret=reddit_secret_key,
    user_agent="web:travelbuddy:v1 (by /u/alaroma)",
)

def makeEndpointFromArgs(endpoint:str, queryArgs: dict = {}):
    queryArgsAsPieces = []
    queryIdx = 0
    for queryArgKey,queryArgValue in queryArgs.items():
        if queryIdx == 0:
            queryArgsAsPieces.append('?');
        else:
            queryArgsAsPieces.append('&');
        
        queryArgsAsPieces.append(queryArgKey)
        queryArgsAsPieces.append('=')
        queryArgsAsPieces.append(str(queryArgValue))
        queryIdx += 1
    

    return endpoint + ''.join(queryArgsAsPieces)


def search_ipinfo(ip_address):
    full_search_url = makeEndpointFromArgs(f"{ipinfo_base_endpoint}/{ip_address}", {
        "token": ipinfo_key
    })

    ipinfo_response:SampleIpinfoResponse = requests.request('GET', full_search_url).json()
    latLongSplit = ipinfo_response["loc"].split(",")
    return (latLongSplit[0], latLongSplit[1])

def search_google_geo(location):
    full_search_url = makeEndpointFromArgs(google_geocode_base_endpoint, {
        "address": location,
        "key": google_key
    })
    google_response: SampleGoogleGeocodingResponse = requests.request('GET', full_search_url).json()
    foundLatitude=None
    foundLongitude=None
    try:
        foundLatitude = google_response["results"][0]["geometry"]["location"]["lat"]
        foundLongitude = google_response["results"][0]["geometry"]["location"]["lng"]
    except Exception as e:
        print(e)
    return (foundLatitude, foundLongitude)

def search_google_nearby_places(query_args):
    full_search_url = f"{google_nearby_search_endpoint}"

    latitude = query_args[latitude] #Test vals 42.8818 
    longitude = query_args[longitude] # -78.8820 
    location_types: List[LocationType] = ["restaurant"] # restaurant | coffee_shop | ice_cream_shop | tourist_attraction
    radius = query_args[radius] if "radius" in query_args else 1000.0 #Default value
    result_count = 20

    json_data = json.dumps({
        "includedTypes": location_types,
        "maxResultCount": result_count,
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": latitude,
                    "longitude": longitude
                },
                "radius": radius
            }
        }
    })
    
    # google_response = requests.post(full_search_url, headers={
    #     "X-Goog-Api-Key": f"{google_key}",
    #     'X-Goog-FieldMask': 'places.id',
    #     'Content-Type': 'application/json',
    # }, data=json_data)
    # parsed_response = google_response.json()
    with open("./api_utils/samples/google_nearby_search.json", 'r') as sample_json:
        parsed_response = json.load(sample_json)

    return parsed_response

# Given a location name, this function queries the Reddit API to identify the most likely subreddit belonging
# to the desired location.
def search_reddit_subreddits(location_name: str):
    full_endpoint = makeEndpointFromArgs(f"{reddit_base_endpoint}/subreddits/search.json", {
        "q": location_name
    })

    location_name_parts = get_separate_location_parts(location_name)

    #Get list of subreddits
    reddit_response: RedditSubredditSearchResult = requests.get(url=full_endpoint).json()
    subreddit_list = reddit_response["data"]["children"]
        
    #Filter out by string similarity/inclusion on subreddit name,
    # title, header_title, description; filter out below certain threshold
    def filter_irrelevant_subreddits(subreddit: SubredditSearchChild):
        subreddit_data = subreddit["data"]

        full_string = f'''{subreddit_data["display_name"]}
{subreddit_data["public_description"]}
{subreddit_data["description"]}
{subreddit_data["header_title"]}'''
        target_name_pieces = len(location_name_parts)
        count_found = 0
        for piece in location_name_parts:
            if piece in full_string:
                count_found += 1
        if count_found == target_name_pieces:
            return True
        else:
            return False
        
    relevant_subreddits: List[SubredditSearchChild] = list(filter(filter_irrelevant_subreddits, subreddit_list))
    #Sort subreddits by subscriber count, select first one
    if len(relevant_subreddits) > 0:
        sorted_subreddits_by_subscribers: List[SubredditSearchChild] = sorted(relevant_subreddits, key=lambda x: x["data"]["subscribers"], reverse=True)
        return (sorted_subreddits_by_subscribers[0], None)
    else:
        #If no results left after filtering, sort by popularity and use first;
        # also, include location name in future queries
        sorted_subreddits_by_subscribers: List[SubredditSearchChild] = sorted(subreddit_list, key=lambda x: x["data"]["subscribers"], reverse=True)
        return (sorted_subreddits_by_subscribers[0], location_name)

def get_comments_for_post(post_id):
    results = reddit.submission(post_id)
    raw_comments = results.comments
    text_comments = list(map(lambda x: x.body, results.comments))
    return (text_comments, raw_comments)


# This function searches the subreddit of the location for posts identifying well-received 
# places of interest, including restaurants, coffee shops, etc...
def search_reddit_subreddit_posts(subreddit: SubredditSearchChild, location_name: str, use_location_name=False):
    subreddit_name = subreddit["data"]["display_name"]
    location_to_use = f'{location_name} ' if use_location_name else ''
    info_query = f'{location_to_use}best restaurants'
    full_endpoint = makeEndpointFromArgs(f"{reddit_base_endpoint}/r/{subreddit_name}/search.json", {
        "q": info_query,
        "restrict_sr": 1
    })

    #Select n top posts
    NUMBER_OF_POSTS = 5
    reddit_response:RedditSubredditRestrictedSearch = requests.get(url=full_endpoint).json()
    post_list:List[PostChild] = reddit_response["data"]["children"]
    sorted_post_by_date = sorted(post_list, key=lambda x: x["data"]["created_utc"], reverse=True)
    posts_to_use = sorted_post_by_date[0:NUMBER_OF_POSTS]
    
    #For each post, collect comments
    def handle_single_post(post:PostChild):
        post_id = post["data"]["id"]
        (text_comments, raw_comments) = get_comments_for_post(post_id)
        return {
            "Post": post,
            "Commments": text_comments
        }
    
    #Return comments as documents
    post_full_info = list(map(handle_single_post, posts_to_use))
    
    return post_full_info 

def search_reddit(query_args):
    latitude = query_args[latitude] #Test vals
    longitude = query_args[longitude]
    # location_types: List[LocationType] = ["restaurant"] # restaurant | coffee_shop | ice_cream_shop | tourist_attraction
    radius = query_args[radius] if "radius" in query_args else 1000.0 #Default value
    (subreddit_to_use, subreddit_name) = search_reddit_subreddits("Buffalo, New York")
    print(subreddit_name)
    use_location_name = False if subreddit_name is None else True
    post_documents = search_reddit_subreddit_posts(subreddit_to_use, subreddit_name, use_location_name)
    return post_documents

def search_all_sources(query_args):
    google_response: GoogleNearbySearch = search_google_nearby_places(query_args)
    reddit_response = search_reddit(query_args)
    full_response = {
            "GoogleMaps": google_response,
            "Reddit": reddit_response
    }
    return full_response

def make_llm_query(all_sources_response):
    google_search_string = []
    google_places = all_sources_response["GoogleMaps"]['places']
    # For each place returned by Google Maps, generate a small markup description 
    # listing the place name, description, hours, and reviews
    for index, place in enumerate(google_places):
        desc = place['editorialSummary']['text']
        displayName = place['displayName']['text']
        hours = place['weekdayDescriptions'] if 'weekdayDescriptions' in place  else ''

        reviews = '\n'.join(map(lambda rev: f'- {rev["text"]["text"]}', place['reviews']))

        place_markup = f''' ## {displayName}
        *Description*: {desc}
        *Hours*: {hours}
        *Reviews*: {reviews}
        '''
        google_search_string.append(place_markup)
    
    return '\n'.join(google_search_string)
    
