def get_k_element(arr, low, high):
    p = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high]= arr[high], arr[i]
    return i
def quick_select(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot_index = get_k_element(arr, low, high)
    if pivot_index == k - 1:
            return arr[pivot_index]
    elif pivot_index < k - 1:
            return quick_select(arr, pivot_index+1, high, k)
    else:
            return quick_select(arr, low, pivot_index-1, k) 