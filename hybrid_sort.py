from sorting2 import merge
from selection_and_insertion import selection_sort

def hybrid_sort(arr, low, high, threshold):
    if ((high - low + 1) <= threshold):
        sub_arr = arr[low:high + 1]
        selection_sort(sub_arr, len(sub_arr))
        arr[low:high + 1] = sub_arr
        
    elif low < high:
        mid = (low + high) // 2   
        hybrid_sort(arr, low, mid, threshold)
        hybrid_sort(arr, mid + 1, high, threshold)
        merge(arr, low, mid, high)
