from functools import lru_cache, wraps
import time
import csv

def timer(func):
    """Print the runtime of the decorated function"""
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter() # 2
        run_time = end_time - start_time # 3
        print(f"Finished {func.__name__!r} in {run_time:.8f} secs")
        return value, run_time
    return wrapper_timer

@lru_cache
@timer
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_iterative(n - 2) + fibonacci_iterative(n - 1)

if __name__ == "__main__":
    # Measure execution times for each value of n
    n_values = range(1, 101)
    execution_data = []

    for n in n_values:
        result, time_taken = fibonacci_iterative(n)
        execution_data.append((n, time_taken))
        print("Execution time for n =", n, ":", time_taken, "seconds")

    with open('execution_times.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Value of n', 'Execution Time (seconds)'])
        for data in execution_data:
            writer.writerow(data)
