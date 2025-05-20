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
    # "scraper": "instagram-profile"
}

# Fetch and save page
try:
    response = requests.get(API_ENDPOINT, params=params)
    response.raise_for_status() 
    
    with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as file:
        file.write(response.text)
    
    print(f"\nPage successfully saved to '{OUTPUT_FILE_NAME}'\n")

except RequestException as error:
    print(f"\nFailed to fetch the page: {error}\n")

