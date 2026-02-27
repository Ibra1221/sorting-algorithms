from datetime import datetime
import random
from bubble_sort import bubble_sort
from selection_and_insertion import insertion_sort, selection_sort

sizes = [1000, 2500, 5000,10000,20000]

insertion_times = []
selection_times = []
bubble_times = []

for size in sizes:

    arr = []

    for i in range(size):
        arr.append(random.randint(0,100000))

    arr_2 = arr.copy()
    arr_3 = arr.copy()

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

