import time
import requests

class RetryException(Exception):
    pass

def retry_request(url, max_attempts=3, backoff_factor=1.0):
    attempts = 0
    while attempts < max_attempts:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            attempts += 1
            if attempts == max_attempts:
                raise RetryException(f'Failed to fetch {url} after {max_attempts} attempts')
            time.sleep(backoff_factor * (2 ** (attempts - 1)))