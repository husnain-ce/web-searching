organizations = [
    "Nueva Group Pty Ltd",
    ".au Domain Administration Ltd",
    "1337 Pty Ltd",

]

from bs4 import BeautifulSoup
import requests

def search_website(organization_name):
    query = organization_name + " website"
    
    response = requests.get(f"https://www.google.com/search?q={query}")
    soup = BeautifulSoup(response.content, "html.parser")

    potential_urls = []
    for link in soup.find_all("a", href=True):
        url = link["href"]
        if organization_name.lower() in url.lower():
            potential_urls.append(url)

    return potential_urls

potential_urls = search_website("Nueva Group Pty Ltd")
print(f"Potential URLs for Nueva Group: {potential_urls}")


def user_verification(potential_urls):
    for url in potential_urls:
        is_valid = input(f"Is this the valid website for {organization_name}? ({url}) (y/n): ")
        if is_valid.lower() == "y":
            return url
    return None

valid_url = user_verification(potential_urls)
print(f"Verified website for Nueva Group: {valid_url}")
