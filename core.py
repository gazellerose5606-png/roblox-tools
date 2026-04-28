import time

class PerformanceOptimizer:
    def __init__(self):
        self.execution_times = []

    def time_function(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.execution_times.append(end_time - start_time)
            return result
        return wrapper

    def get_average_time(self):
        return sum(self.execution_times) / len(self.execution_times) if self.execution_times else 0

    def reset_times(self):
        self.execution_times.clear()

optimizer = PerformanceOptimizer()  

@optimizer.time_function  
def sample_function(x):
    total = 0
    for i in range(x):
        total += i * i
    return total

# Example usage:
if __name__ == '__main__':
    sample_function(10000)
    print('Average execution time:', optimizer.get_average_time())
