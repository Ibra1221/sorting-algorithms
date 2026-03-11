def bubble_sort(arr):
    for i in range(len(arr)):
        changed = False
        for j in range(len(arr) - i - 1):
            if(arr[j] > arr[j+1]):
                changed = True
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if(changed == False):
            break

    
