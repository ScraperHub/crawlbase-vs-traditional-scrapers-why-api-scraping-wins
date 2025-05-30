import requests
import json
from requests.exceptions import RequestException

# Configuration
API_TOKEN = "<Normal requests token>"
TARGET_URL = "https://www.google.com/search?q=Mike+Tyson"
API_ENDPOINT = "https://api.crawlbase.com/"

params = {
    "token": API_TOKEN,
    "url": TARGET_URL,
    "scraper": "google-serp",
    "country": "US"
}

# Fetch the content of the page as structured JSON format
try:
    response = requests.get(API_ENDPOINT, params=params)
    response.raise_for_status()

    json_string_content = response.text
    json_data = json.loads(json_string_content)
    pretty_json = json.dumps(json_data, indent=2)
    print(pretty_json)

except RequestException as error:
    print(f"\n Failed to fetch the page: {error}\n")
