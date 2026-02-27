def selection_sort(arr,n):
    for i in range(n-1):
        i_min=i
        for j in range(i+1,n):
            if arr[j]<arr[i_min]:
                i_min=j
                

        if(i!=i_min):
         arr[i],arr[i_min]=arr[i_min],arr[i]
    return arr
def insertion_sort(arr,n):
   for i in range(1,n):
      key=arr[i]
      j=i
      while(j>0 and arr[j-1]>key):
         arr[j]=arr[j-1]
         j-=1  
         arr[j]=key 
