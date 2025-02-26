import random
import time
import matplotlib.pyplot as plt
import numpy as np

def Non_Random_QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return Non_Random_QuickSort(left) + middle + Non_Random_QuickSort(right)

def Random_QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return Random_QuickSort(left) + middle + Random_QuickSort(right)

def Time_measuring(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

sizes = [100, 500, 1000, 5000, 10000]
best_case_times = []
worst_case_times = []
average_case_times = []

for size in sizes:
    best_case = list(range(size))  
    worst_case = list(range(size, 0, -1))  
    average_case = list(np.random.randint(0, size, size)) 
    
    best_case_times.append(Time_measuring(Non_Random_QuickSort, best_case))
    worst_case_times.append(Time_measuring(Non_Random_QuickSort, worst_case))
    average_case_times.append(Time_measuring(Non_Random_QuickSort, average_case))

plt.plot(sizes, best_case_times, label='Best Case')
plt.plot(sizes, worst_case_times, label='Worst Case')
plt.plot(sizes, average_case_times, label='Average Case')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Non Random Pivot version')
plt.legend()
plt.show()
