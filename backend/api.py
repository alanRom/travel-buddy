from math import ceil
import requests
from api_keys import yelp_key, yelp_search_base_endpoint, yelp_details_base_endpoint,google_geocode_base_endpoint, google_key,ipinfo_base_endpoint,ipinfo_key
from types.google_responses import SampleGoogleGeocodingResponse
from types.yelp_response import SampleYelpResponse
from types.ipinfo_response import SampleIpinfoResponse

def search_yelp(search_args):   
    full_search_url = makeEndpointFromArgs(yelp_search_base_endpoint, search_args)
    yelp_response = requests.request('GET', full_search_url, headers={
        "Authorization": f"Bearer {yelp_key}"
    })
    return yelp_response.json()

def get_yelp_business_details(business_id):   
    full_search_url = f"{yelp_details_base_endpoint}/{business_id}"
    yelp_response = requests.request('GET', full_search_url, headers={
        "Authorization": f"Bearer {yelp_key}"
    })
    return yelp_response.json()


def makeEndpointFromArgs(endpoint:str, queryArgs: dict):
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


def search_yelp_api(query_args):
    yelp_search_args = {}
    yelp_keys = [('keyword', 'term'), ('distance', 'radius'), ('category', 'categories')]
    for query_key, yelp_key in yelp_keys:
        if query_key == 'distance':
            yelp_search_args[yelp_key] = str(ceil(float(query_args[query_key]) * 1609.344))
        else:
            yelp_search_args[yelp_key] = query_args[query_key]

    should_auto_locate = query_args["shouldAutoDetectLocation"] == "true"
    auto_location = query_args["auto-location"]
    if should_auto_locate:
        # user_ip = request.remote_addr
        # if (request.access_route):
        #     #return remote ip
        #     user_ip = request.access_route[0]
        # latitude,longitude = search_ipinfo(user_ip)
        autoLatLong = auto_location.split(",")
        latitude = autoLatLong[0]
        longitude = autoLatLong[1]

    else:
        latitude,longitude = search_google_geo(query_args["location"])
        
    yelp_search_args["latitude"] = latitude
    yelp_search_args["longitude"] = longitude
    print(query_args)

    yelp_response: SampleYelpResponse = search_yelp(yelp_search_args)
    return yelp_response

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
