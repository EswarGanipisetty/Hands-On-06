import random

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

def randomized_partition(arr, low, high):
    rand_idx = random.randint(low, high)
    arr[high], arr[rand_idx] = arr[rand_idx], arr[high]
    return partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Original array:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Sorted array using non-randomized pivot:", arr)

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Original array:", arr)
randomized_quicksort(arr, 0, len(arr) - 1)
print("Sorted array using randomized pivot:", arr)
