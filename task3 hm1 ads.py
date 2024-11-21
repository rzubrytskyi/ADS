import random
import time

def generate_sorted_array(size, lower_bound=1, upper_bound=1000000):
    array = [random.randint(lower_bound, upper_bound) for _ in range(size)]
    return sorted(array)

def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def measure_execution_time():
    sizes = [1000, 10000, 100000, 1000000]
    for size in sizes:
        arr = generate_sorted_array(size)
        target = arr[-1]
        start_time = time.time()
        linear_search(arr, target)
        linear_time = time.time() - start_time
        start_time = time.time()
        binary_search(arr, target)
        binary_time = time.time() - start_time
        print(f"Array Size: {size}")
        print(f"Linear Search Time: {linear_time:.6f} seconds")
        print(f"Binary Search Time: {binary_time:.6f} seconds")

measure_execution_time()