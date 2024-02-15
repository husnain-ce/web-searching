import requests
from bs4 import BeautifulSoup
from difflib import get_close_matches

def find_matching_urls(query, target_domain):
    # Assume headers and proxies are defined as in your original script
    headers = {
        "User-Agent": "your user agent string here"
    }
    proxies = {
        # Your proxy configuration if necessary
    }

    url = "https://www.google.com/search?q=" + query
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', href=True)
            all_urls = []
            for link in links:
                href = link['href']
                if 'http' in href and '/url?q=' in href:
                    start = href.find('/url?q=') + len('/url?q=')
                    end = href.find('&', start)
                    url = href[start:end] if end != -1 else href[start:]
                    all_urls.append(url)

            # Get close matches to the target domain name from the extracted URLs
            close_matches = get_close_matches(target_domain, all_urls, n=5, cutoff=0.1)  # Adjust n and cutoff as needed

            return close_matches
    except Exception as e:
        print("An error occurred:", str(e))
        return []

# Example usage
target_domain = "example.com"
query = "python org"
matching_urls = find_matching_urls(query, target_domain)
for url in matching_urls:
    print(url)
