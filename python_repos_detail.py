# Working with APIs: Processing an API Response

# Import Python Requests module
import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status Code: {r.status_code}')

# Store API response in a variable
response_dict = r.json()
print(f'Total repositories: {response_dict["total_count"]}')

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

# Examine the first repository
repo_dict = repo_dicts[0]

print('\nSelected information about first repository: ')
print(f'\t- Name: {repo_dict["name"]}')
print(f'\t- Owner: {repo_dict["owner"]["login"]}')
print(f'\t- Stars: {repo_dict["stargazers_count"]}')
print(f'\t- Repository: {repo_dict["html_url"]}')
print(f'\t- Created: {repo_dict["created_at"]}')
print(f'\t- Updated: {repo_dict["updated_at"]}')
print(f'\t- Description: {repo_dict["description"]}')