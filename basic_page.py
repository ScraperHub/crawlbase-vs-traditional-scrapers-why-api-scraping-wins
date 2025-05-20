import requests
from requests.exceptions import RequestException

# Configuration
TARGET_URL = "https://www.google.com/search?q=Mike+Tyson"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

# Fetch the HTML content of the page
try:
    response = requests.get(TARGET_URL, headers=HEADERS)
    response.raise_for_status()
    
    html_content = response.text
    print(html_content)  # Output the raw HTML content

    # To extract structured data (e.g., search results),
    # use a parser like Beautiful Soup on `html_content`.

except RequestException as error:
    print(f"\n Failed to fetch the page: {error}\n")
