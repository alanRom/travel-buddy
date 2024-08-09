
import functions_framework
import json
from api_utils.api import search_google_nearby_places, search_reddit
from markupsafe import escape

@functions_framework.http
def search_apis(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_args = request.args

    google_response = search_google_nearby_places(request_args)
    reddit_response = search_reddit(request_args)

    full_response = {
        "GoogleMaps": google_response,
        "Reddit": reddit_response
    }
    return json.dumps(full_response)

# 