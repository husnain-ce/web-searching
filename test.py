import requests

# Google Custom Search API endpoint
API_ENDPOINT = "https://www.googleapis.com/customsearch/v1"
API_KEY = ""  # Your API key
CSE_ID = ""  # Your Custom Search Engine ID

# Function to search for an organization's website URL
def search_for_website(organization_name):
    params = {
        'key': API_KEY,
        'cx': CSE_ID,
        'q': organization_name
    }
    response = requests.get(API_ENDPOINT, params=params)
    result = response.json()

    # Extract the first search result URL
    if 'items' in result and len(result['items']) > 0:
        print(result['items'][0]['link'])
        print(result)
        return result['items'][0]['link']
    else:
        print(result)
        return "No URL found"

# Read organization names from a text file
with open('organizations.txt', 'r') as file:
    organization_names = file.readlines()

# Search for URLs and write them to another text file
with open('organization_urls.txt', 'w') as file:
    for name in organization_names:
        url = search_for_website(name)
        file.write(f"{name.strip()}: {url}\n")

print("URLs have been written to organization_urls.txt")
