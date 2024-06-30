import requests
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

def search_reddit_subreddits(location_name):
    full_endpoint = makeEndpointFromArgs(f"{reddit_base_endpoint}/subreddits/search.json", {
        "q": location_name
    })

    #Get list of subreddits

    
    #Filter out by string similarity/inclusion on subreddit name,
    # title, header_title, description; filter out below certain threshold
    
    #Sort subreddits by subscriber count, select first one

    #If no results left after filtering, sort by popularity and use first;
    # also, include location name in future queries

    pass

def search_reddit_subreddit_for_places(subreddit_name, location_name: str, use_location_name=False):
    
    location_to_use = f'{location_name} ' if use_location_name else ''
    info_query = f'{location_to_use}best restaurants'
    full_endpoint = makeEndpointFromArgs(f"{reddit_base_endpoint}/r/{subreddit_name}/search.json", {
        "q": info_query,
        "restrict_sr": 1
    })

    
    pass