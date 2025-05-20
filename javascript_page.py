import requests
from requests.exceptions import RequestException

# Configuration
TARGET_URL = "https://www.instagram.com/leomessi"
OUTPUT_FILE_NAME = "output.html"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

# Fetch and save page
try:
    response = requests.get(TARGET_URL, headers=HEADERS)
    response.raise_for_status()
    
    with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as file:
        file.write(response.text)
    
    print(f"\nPage successfully saved to '{OUTPUT_FILE_NAME}'\n")

except RequestException as error:
    print(f"\nFailed to fetch the page: {error}\n")
