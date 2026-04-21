import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, backoff_factor=0.3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException:
            if attempt < max_retries - 1:
                time.sleep(backoff_factor * (2 ** attempt))
            else:
                raise
