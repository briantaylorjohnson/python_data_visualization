# The Hacker News API

# Import the Python Requests module
import requests

# Import the Python JSON module
import json

# Make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f'Status Code: {r.status_code}')

# Explore the structure of the data
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'

with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)