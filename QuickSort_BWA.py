import time
import random
import matplotlib.pyplot as plt
import sys


sys.setrecursionlimit(10**6)  


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def generate_best_case(n):
    return list(range(1, n + 1))

def generate_worst_case(n):
    return list(range(n, 0, -1))

def generate_average_case(n):
    return random.sample(range(1, n + 1), n)

def benchmark_sorting(sort_function, input_generator, sizes, repetitions):
    results = []
    for n in sizes:
        total_time = 0
        for _ in range(repetitions):
            arr = input_generator(n)
            start_time = time.time()
            sort_function(arr, 0, len(arr) - 1)
            end_time = time.time()
            total_time += end_time - start_time
        average_time = total_time / repetitions
        results.append(average_time)
    return results

sizes = [100, 500, 1000, 2000, 5000]
repetitions = 10

best_case_times = benchmark_sorting(quicksort, generate_best_case, sizes, repetitions)
worst_case_times = benchmark_sorting(quicksort, generate_worst_case, sizes, repetitions)
average_case_times = benchmark_sorting(quicksort, generate_average_case, sizes, repetitions)

plt.plot(sizes, best_case_times, label='Best Case')
plt.plot(sizes, worst_case_times, label='Worst Case')
plt.plot(sizes, average_case_times, label='Average Case')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Benchmark')
plt.legend()
plt.show()
