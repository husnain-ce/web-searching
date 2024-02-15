import requests
from concurrent.futures import ThreadPoolExecutor

def query_api(company, file_path,file_path_not_found):
    base_url = "https://autocomplete.clearbit.com/v1/companies/suggest?query="
    try:
        response = requests.get(base_url + requests.utils.quote(company.strip()))
        response.raise_for_status()
        data = response.json()
        if data:
            result = f"{company}: {data[0]['domain']}\n"
            # Write the result to a file
            with open(file_path, 'a') as file:
                file.write(result)
        else:
            result = f"{company}: No result found\n"
            # Write the result to a file
            with open(file_path_not_found, 'a') as file:
                file.write(result)
    except requests.RequestException:
        result = f"{company}: Error querying the API\n"
    
    

def read_company_names(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def main():
    company_names = read_company_names("organizations.txt")  # Adjust path as necessary
    output_file_path = "urls.txt"  # Adjust path as necessary
    output_not_found_file_path = "not_found.txt"  # Adjust path as necessary
    
    # Clear the output file before starting
    open(output_file_path, 'w').close()
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Use a lambda to pass the additional argument (output file path) to query_api
        executor.map(lambda company: query_api(company, output_file_path, output_not_found_file_path), company_names)

if __name__ == "__main__":
    main()
