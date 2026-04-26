import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Function {func.__name__} executed in {{end - start}} seconds.')
        return result
    return wrapper

@timeit
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@timeit
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

@timeit
def sum_numbers(numbers):
    return sum(numbers)

if __name__ == '__main__':
    print(fibonacci(35))
    print(factorial(10))
    print(sum_numbers(range(1000000)))