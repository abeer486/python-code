import requests

### Read through Github's most started python repos

# Make an API call and save the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code )

# Store API response in variable
response_dict = r.json()
print("Total respos:", response_dict['total_count'])

# Process results
# print(response_dict.keys())


# Explore information about the repos.
repo_dicts = response_dict['items']
print("Repos returned:", len(repo_dicts))

repo_dict = repo_dicts[0]
''' print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
 '''

print("\Selected information about first repo:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Description:', repo_dict['description'])
