import requests
from bs4 import BeautifulSoup
import time
import random
from concurrent.futures import ThreadPoolExecutor
import time

# List of user agents to rotate
user_agents = [
  

]

def find_first_url(query):
    search_url = f"https://www.google.com/search?q={query}+site%3A*"
    # Randomly select a user agent
    headers = {'User-Agent': random.choice(user_agents)}
    
    try:
        time.sleep(5)  # Be polite and don't overwhelm the server
        response = requests.get(search_url, headers=headers)
        if response.status_code == 200:
            print("Doone")
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if 'http' in href and '/url?q=' in href:
                    start = href.find('/url?q=') + len('/url?q=')
                    end = href.find('&', start)
                    url = href[start:end] if end != -1 else href[start:]
                    return url
            return "No valid URL found"
        else:
            return "Failed to retrieve content"
    except Exception as e:
        return str(e)



def process_organization(name):
    url = find_first_url(name)
    result = f"{name}: {url}\n"
    with open("results.txt", 'a') as file:  # Open file in append mode
        file.write(result)

def main():
    file_path = 'new-org.txt'  # Replace 'new-org.txt' with the path to your text file
    with open(file_path, 'r') as file:
        organization_names = [line.strip() for line in file.readlines()]

    # Clear the results file before writing new results
    open("results.txt", 'w').close()

    # Using ThreadPoolExecutor to process organizations in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_organization, organization_names)

if __name__ == "__main__":
    main()
