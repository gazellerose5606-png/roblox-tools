import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            attempt += 1
            if attempt == retries:
                raise NetworkError(f'Failed to fetch data from {url} after {retries} attempts')
            time.sleep(delay)
