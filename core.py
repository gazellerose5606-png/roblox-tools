import time

class PerformanceOptimizer:
    def __init__(self):
        self.execution_times = []

    def track_time(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.execution_times.append(end_time - start_time)
            return result
        return wrapper

    def average_execution_time(self):
        if not self.execution_times:
            return 0
        return sum(self.execution_times) / len(self.execution_times)

    def clear_times(self):
        self.execution_times = []

optimizer = PerformanceOptimizer()

@optimizer.track_time
def some_heavy_function(data):
    total = sum(data)
    return total

if __name__ == '__main__':
    print(some_heavy_function(range(1000000)))
    print(f'Average execution time: {optimizer.average_execution_time()} seconds')
