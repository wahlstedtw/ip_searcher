import requests, os
from requests.exceptions import HTTPError

# Polling helpers to grab remote data

def poll_url(url, payload):
    print("Polling URL")

    try:
        r = requests.get(url,payload)
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        # There is no value in continuing to run with no data, bailing here
        raise SystemExit
    except Exception as err:
        print(f'Other error occured: {err}')
        # There is no value in continuing to run with no data, bailing here
        raise SystemExit
    else:
        print(f'Success! Status Code: {r.status_code}')

    return r.json()
