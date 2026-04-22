import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@time_it
def optimized_function(data):
    return {key: value for key, value in data.items() if value is not None}

@time_it
def process_data(data):
    results = []
    for item in data:
        results.append(optimized_function(item))
    return results

@time_it
def main(data_collection):
    return process_data(data_collection)