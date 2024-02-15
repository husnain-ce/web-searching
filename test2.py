import requests
import time
from bs4 import BeautifulSoup

from random import randint

# List of user agents to rotate
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
]

# Function to perform a Google search
def google_search(query):
    url = "https://www.google.com/search?q=" + query
    headers = {'User-Agent': user_agents[randint(0, len(user_agents) - 1)]}
    proxies = {
        # Add your proxy settings here if you're using proxies
    }
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if 'http' in href and '/url?q=' in href:
                    start = href.find('/url?q=') + len('/url?q=')
                    print(start)
                    
                    end = href.find('&', start)
                    url = href[start:end] if end != -1 else href[start:]
                    print(url)
                    return url
            print("Search successful!")
        else:
            print("Failed to perform the search. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))

# Main function
def main():
    queries = ["python tutorial", "data science", "machine learning"]
    for query in queries:
        google_search(query)
        # Add a delay between requests to avoid being blocked
        time.sleep(randint(5, 10))

if __name__ == "__main__":
    main()
