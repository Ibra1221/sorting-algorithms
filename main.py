from datetime import datetime
import random
from bubble_sort import bubble_sort
from selection_and_insertion import insertion_sort, selection_sort
from sorting2 import quick_sort, heap_sort, merge_sort
import matplotlib.pyplot as plt


sizes = [1000,5000,10000,20000,30000]


insertion_times = []
selection_times = []
bubble_times = []
quick_times = []
heap_times = []
merge_times = []


for size in sizes:

    arr = []

    for i in range(size):
        arr.append(random.randint(0,100000))

    arr_2 = arr.copy()
    arr_3 = arr.copy()
    arr_4 = arr.copy()
    arr_5 = arr.copy()
    arr_6 = arr.copy()
    arr_7 = arr.copy()

    start_time = datetime.now()
    bubble_sort(arr)
    end_time = datetime.now()

    difference = (end_time-start_time).total_seconds() *1000

    bubble_times.append(difference)

    print(f"Running time for Bubble Sort is {difference} ms")

    start_time = datetime.now()
    insertion_sort(arr_2, len(arr_2))
    end_time = datetime.now()

    difference = (end_time-start_time).total_seconds() *1000

    insertion_times.append(difference)

    print(f"Running time for Insertion Sort is {difference} ms")

    start_time = datetime.now()
    selection_sort(arr_3, len(arr_3 ))
    end_time = datetime.now()

    difference = (end_time-start_time).total_seconds() *1000

    selection_times.append(difference)

    print(f"Running time for Selection Sort is {difference} ms")
    
    
    
    start_time = datetime.now()
    quick_sort(arr_4, 0, len(arr_4) - 1)
    end_time = datetime.now()
    difference = (end_time-start_time).total_seconds() *1000
    quick_times.append(difference)
    print(f"Running time for Quick Sort is {difference} ms")
    

    start_time = datetime.now()
    heap_sort(arr_5)
    end_time = datetime.now()
    difference = (end_time-start_time).total_seconds() *1000
    heap_times.append(difference)
    print(f"Running time for Heap Sort is {difference} ms")
    
    start_time = datetime.now()
    merge_sort(arr_6, 0, len(arr_6) - 1)
    end_time = datetime.now()
    difference = (end_time-start_time).total_seconds() *1000
    merge_times.append(difference)
    print(f"Running time for Merge Sort is {difference} ms")
    
    

plt.plot(sizes, bubble_times, marker='o', label="Bubble")
plt.plot(sizes, insertion_times, marker='o', label="Insertion")
plt.plot(sizes, selection_times, marker='o', label="Selection")
plt.plot(sizes, quick_times, marker='o', label="Quick")
plt.plot(sizes, heap_times, marker='o', label="Heap")
plt.plot(sizes, merge_times, marker='o', label="Merge")

plt.xlabel("Array Size")
plt.ylabel("Time (ms)")
plt.legend()
plt.show()