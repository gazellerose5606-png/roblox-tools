import requests
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except requests.RequestException:
                    attempts += 1
                    if attempts < max_attempts:
                        time.sleep(delay)
            raise Exception('Max retry attempts exceeded')
        return wrapper
    return decorator

@retry(max_attempts=5, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()