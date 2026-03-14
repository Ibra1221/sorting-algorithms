import random
from hybrid_sort import hybrid_sort
from quick_select import quick_select
from sorting2 import merge_sort
from datetime import datetime

hybrid_times = []
quick_select_times = [] 
merge_times = []
sizes = [1000, 5000, 10000, 20000, 30000]

for size in sizes:
    arr1 = [random.randint(0, 100000) for _ in range(size)]
    start_time = datetime.now()
    hybrid_sort(arr1, 0, len(arr1) - 1, 6)
    end_time = datetime.now()
    difference = (end_time - start_time).total_seconds() * 1000
    hybrid_times.append(difference)
    print(f"Size {size} - Running time for Hybrid Sort: {difference} ms")
    arr2 = [random.randint(0, 100000) for _ in range(size)]
    start_time = datetime.now()
    quick_select(arr2, 0, len(arr2) - 1, 3)
    end_time = datetime.now()
    difference = (end_time - start_time).total_seconds() * 1000
    quick_select_times.append(difference)
    print(f"Size {size} - Running time for Quick Select: {difference} ms")
    arr3 = [random.randint(0, 100000) for _ in range(size)]
    start_time = datetime.now()
    merge_sort(arr3, 0, len(arr3) - 1)
    end_time = datetime.now()
    difference = (end_time - start_time).total_seconds() * 1000
    merge_times.append(difference)
    print(f"Size {size} - Running time for Merge Sort: {difference} ms")