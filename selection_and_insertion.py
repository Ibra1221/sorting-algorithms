def selection_sort(arr,n):
    for i in range(n-1):
        i_min=i
        for j in range(i+1,n):
            if arr[j]<arr[i_min]:
                i_min=j
                

        if(i!=i_min):
         arr[i],arr[i_min]=arr[i_min],arr[i]
    return arr

def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr