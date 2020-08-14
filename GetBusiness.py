import json
import requests
# import requests

def lambda_handler(event, context):
    # TODO implement
    # Define a business ID
    
    print(event)
    print(event['context']['http-method'])
    print(event['body-json']['location'])

    API_KEY = 'Your-API-Key'
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'bearer %s' % API_KEY}
    
    # Define my parameters of the search
    # BUSINESS SEARCH PARAMETERS - EXAMPLE
    PARAMETERS = {'term': 'food',
                 'limit': 20,
                 'radius': 10000,
                 'location': event['body-json']['location']} #{'body-json': {'location': 'Ohio'}

    response = requests.get(url = ENDPOINT,
                            params = PARAMETERS,
                            headers = HEADERS)
    
    # Conver the JSON String
    business_data = response.json()
    ans = {}
    for business in business_data['businesses']:
        print(business['id'], business['name'])
        ans[business['id']] = business['name']
    print("ans")
    print(ans)
    return ans
