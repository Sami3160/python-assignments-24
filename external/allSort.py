def merge_sort(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
        
        i=j=k=0
        while( i< len(left) and j<len(right)):
            if(left[i]<right[j]):
                arr[k]=left[i]
                i+=1
                k+=1
            else:
                arr[k]=right[j]
                k+=1
                j+=1
        while(j<len(right)):
            arr[k]=right[j]
            k+=1
            j+=1
        while(i<len(left)):
            arr[k]=left[i]
            i+=1
            k+=1





def insertion_sort(arr):
    for i in range (1, len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr=[2,5,9,12,1,6,4]
insertion_sort(arr)
print(arr)