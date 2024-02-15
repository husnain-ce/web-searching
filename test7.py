import requests
import time
def query_clearbit(company_names):
    base_url = "https://autocomplete.clearbit.com/v1/companies/suggest?query="
    
    for company in company_names:
        # Encode the company name to handle spaces and special characters
        encoded_company = requests.utils.quote(company)
        full_url = base_url + encoded_company
        
        try:
            response = requests.get(full_url)
            response.raise_for_status()  # Raises an error for bad responses
            
            # Assuming the response is JSON and contains a list of companies
            companies = response.json()
            
            if companies:
                print(f"Querying: {company}")
                print("Domain found:", companies[0]['domain'])
            else:
                print(f"Querying: {company}")
                print("No result found")
                
        except requests.RequestException as e:
            print(f"Error querying {company}: {e}")
        
        # Sleep to avoid hitting the API rate limit
        time.sleep(1)

# List of company names
company_names = [
    "1337",
    "3 Crowns Technologies",
    "325 Holdings Pty Ltd & 325 IP Pty Ltd & 325 Technology",
    "37South",
    "5 Elk",
    "5G Network Operations Pty Ltd",
    "6clicks Pty Ltd",
    "Cyber Evangelists"
]

query_clearbit(company_names)
