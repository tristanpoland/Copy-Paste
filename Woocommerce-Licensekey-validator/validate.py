import requests
from requests.auth import HTTPBasicAuth

def CheckUserKey(Key, url):
    # Set the base URL for the API
    base_url = str(url) + '/wp-json/lmfwc/v2'
    print(base_url)

    # Set the API key and secret (They are only usable to check license status)
    api_key = ''
    api_secret = ''

    # Set the license key to validate
    license_key = Key

    # Make a GET request to the validate endpoint with the license key as a parameter
    response = requests.get(f'{base_url}/licenses/validate/{license_key}', auth=HTTPBasicAuth(api_key, api_secret))

    # Check if the request was successful
    if response.status_code == 200:
        # Get the JSON data from the response
        data = response.json()
        print(data)
        # Check if the license key is valid
        if data['success']:
            print('License key is valid')
            return True
        else:
            print('License key is not valid')
            return False
    else:
        print(f'The server returned an error while validating your license key: {response.status_code} - {response.text}')
