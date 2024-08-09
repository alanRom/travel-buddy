from typing import List
import requests

from api_utils.types.reddit_subreddit_search_response import RedditSubredditSearchResult, SubredditSearchChild
from api_utils.utils import get_separate_location_parts
from .api_keys import google_geocode_base_endpoint, google_key, google_nearby_search_endpoint, ipinfo_base_endpoint,ipinfo_key, reddit_base_endpoint
from .types.google_geocoding_responses import SampleGoogleGeocodingResponse
from .types.ipinfo_response import SampleIpinfoResponse
import json
from difflib import SequenceMatcher


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

    latitude = 42.8818 #query_args[latitude] #Test vals
    longitude = -78.8820 #query_args[longitude]
    location_types = ["restaurant"] # restaurant | coffee_shop | ice_cream_shop | tourist_attraction
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
        sorted_subreddits_by_subscribers = sorted(relevant_subreddits, key=lambda x: x["data"]["subscribers"], reverse=True)
        return (sorted_subreddits_by_subscribers[0], None)
    else:
        #If no results left after filtering, sort by popularity and use first;
        # also, include location name in future queries
        sorted_subreddits_by_subscribers = sorted(subreddit_list, key=lambda x: x["data"]["subscribers"], reverse=True)
        return (sorted_subreddits_by_subscribers[0], location_name)

# This function searches the subreddit of the location for posts identifying well-received 
# places of interest, including restaurants, coffee shops, etc...
def search_reddit_subreddit_posts(subreddit_name, location_name: str, use_location_name=False):
    location_to_use = f'{location_name} ' if use_location_name else ''
    info_query = f'{location_to_use}best restaurants'
    full_endpoint = makeEndpointFromArgs(f"{reddit_base_endpoint}/r/{subreddit_name}/search.json", {
        "q": info_query,
        "restrict_sr": 1
    })

    #Select n top posts
    NUMBER_OF_POSTS = 5
    reddit_response = requests.get(url=full_endpoint).json()
    post_list = reddit_response["data"]["children"]
    sorted_post_by_date = sorted(post_list, key=lambda x: x["data"]["created_utc"], reverse=True)
    posts_to_use = sorted_post_by_date[0:NUMBER_OF_POSTS]
    
    #For each post, collect comments

    #Return comments as documents
    
    pass 

def search_reddit(query_args):
    latitude = 42.8818 #query_args[latitude] #Test vals
    longitude = -78.8820 #query_args[longitude]
    location_types = ["restaurant"] # restaurant | coffee_shop | ice_cream_shop | tourist_attraction
    radius = query_args[radius] if "radius" in query_args else 1000.0 #Default value
    result_count = 20
    (subreddit_to_use, subreddit_name) = search_reddit_subreddits("Buffalo, New York")
    return subreddit_to_use
