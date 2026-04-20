import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, backoff_factor=0.3):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            retries += 1
            wait = backoff_factor * (2 ** (retries - 1))
            time.sleep(wait)
            if retries == max_retries:
                raise RuntimeError(f'Failed to retrieve data from {url} after {max_retries} attempts')
