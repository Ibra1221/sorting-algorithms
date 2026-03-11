#Quick Sort
import random


def quick_sort(A, l, h):
    if l < h:
        m = partition(A, l, h)
        quick_sort(A, l, m - 1)
        quick_sort(A, m + 1, h)


def random_partition(A, l, h):
    i = random.randint(l, h)   # b5tar random index
    A[h], A[i] = A[i], A[h]    # bdl pivot with last element
    return partition(A, l, h)


def partition(A, l, h):
    x = A[h]        # pivot
    j = l - 1

    for i in range(l, h):
        if A[i] < x:
            j = j + 1
            A[i], A[j] = A[j], A[i]
    j = j + 1
    A[j], A[h] = A[h], A[j]
    return j
#--------------------------------------------------------------------------------------
# Heap Sort
def heapify(arr, n, i):
    largest = i        
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < n and arr[left] >arr[largest]:
        largest = left
    if right < n and arr[right] >arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    build_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
#--------------------------------------------------------------------------------------
# Merge Sort
def merge(arr, low, mid, high):
    nL = mid - low + 1  
    nR = high - mid     
    
    L = [0] * nL
    R = [0] * nR
    
    for i in range(nL):
        L[i] = arr[low + i]
    
    for j in range(nR):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = low
    
    while i < nL and j < nR:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    
    while i < nL:
        arr[k] = L[i]
        i += 1
        k += 1
    
    
    while j < nR:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2   
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
