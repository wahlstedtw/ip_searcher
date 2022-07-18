# Script to fetch some json from https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix and parse it
import sys, requests
from argument import arg_handler
from poller import poll
from storage import datastore
from searcher import search

URL = "https://stat.ripe.net/data/country-resource-list/data.json"
payload = {'resource': 'us', "v4_format":"prefix"}

# Strip off the script name to get to the argument then
#  do some sanity checking.
ip_arg = arg_handler.process_args()

# Poll a given URL with a payload
url_data = poll.poll_url(URL, payload)

# Process and store data pulled from URL
url_data = datastore.store(url_data)

# # Search data for given IP
result = search.for_ipv4(url_data, ip_arg)

print(f"Results: {result}")
