import requests
import time
from requests.exceptions import RequestException

def retry_request(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise e

# Example usage:
#if __name__ == '__main__':
#    data = retry_request('https://jsonplaceholder.typicode.com/posts')
#    print(data)