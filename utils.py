import time
import requests

def retry_request(url, retries=3, backoff=2):
    for i in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if i < retries - 1:
                time.sleep(backoff ** i)
            else:
                raise e
