from datetime import datetime
import random
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

x = int(input("Enter size of the array"))

arr = []

for i in range(x):
    arr.append(random.randint(0,100000))

arr_2 = arr.copy()
arr_3 = arr.copy()

start_time = datetime.now()
bubble_sort(arr)
end_time = datetime.now()

difference = (end_time-start_time).total_seconds() *1000

print(f"Running time for Bubble Sort is {difference} ms")

start_time = datetime.now()
insertion_sort(arr)
end_time = datetime.now()

difference = (end_time-start_time).total_seconds() *1000

print(f"Running time for Bubble Sort is {difference} ms")

start_time = datetime.now()
selection_sort(arr)
end_time = datetime.now()

difference = (end_time-start_time).total_seconds() *1000

print(f"Running time for Bubble Sort is {difference} ms")

