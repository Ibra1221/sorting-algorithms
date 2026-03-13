import random

from hybrid_sort import hybrid_sort
from datetime import datetime

hybrid_times = []
sizes = [1000,5000,10000,20000,30000]

for size in sizes:
    arr = []
    for i in range(size):
        arr.append(random.randint(0,100000))


    start_time = datetime.now()
    hybrid_sort(arr, 0, len(arr) - 1, 6)
    end_time = datetime.now()
    difference = (end_time-start_time).total_seconds() *1000
    hybrid_times.append(difference)
    print(f"Running time for Hybrid Sort is {difference} ms")
