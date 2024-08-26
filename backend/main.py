
import functions_framework
import json
from api_utils.api import make_llm_query, search_all_sources
from api_utils.api_keys import is_production
import os 

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
    if is_production:
        full_response = search_all_sources(request_args)

    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))

        with open(os.path.join(dir_path,'api_utils','samples','output_reddit_results.json'), 'r') as sample_fi:
            full_response = json.load(sample_fi)

    return json.dumps(full_response)

# 
def test_llm_query():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path,'api_utils','samples','output_reddit_results.json'), 'r') as sample_fi:
        full_response = json.load(sample_fi)
    query = make_llm_query(full_response)
    print(query)

if __name__ == '__main__':
    test_llm_query()