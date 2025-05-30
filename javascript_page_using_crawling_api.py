import json
import requests
from requests.exceptions import RequestException

# Configuration
API_TOKEN = "<JavaScript requests token>"
TARGET_URL = "https://www.instagram.com/leomessi"
API_ENDPOINT = "https://api.crawlbase.com/"
OUTPUT_FILE_NAME = "output.html"

params = {
    "token": API_TOKEN,
    "url": TARGET_URL,
    ## Uncomment the code below when output to console
    # "scraper": "instagram-profile"
}

# Fetch and save page
try:
    response = requests.get(API_ENDPOINT, params=params)
    response.raise_for_status() 
    
    ## START: Output to file
    with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as file:
        file.write(response.text)
    ## END: Output to file

    print(f"\nPage successfully saved to '{OUTPUT_FILE_NAME}'\n")

    ## Uncomment the code below when output to console
    ## START: Output to console
    # json_string_content = response.text
    # json_data = json.loads(json_string_content)
    # pretty_json = json.dumps(json_data, indent=2)
    # print(pretty_json)
    ## END: Output to console

except RequestException as error:
    print(f"\nFailed to fetch the page: {error}\n")
