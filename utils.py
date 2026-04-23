import time
import requests

class NetworkError(Exception):
    pass

def retry_request(method, url, **kwargs):
    retries = 5
    delay = 2
    for i in range(retries):
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except requests.RequestException:
            if i < retries - 1:
                time.sleep(delay)
                delay *= 2
            else:
                raise NetworkError(f'Failed to connect after {retries} attempts')
