               
def InsertionSort(array):
    n = len(array)
    for i in range(1, n):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    return array        
def BubbleSort(array):
    n=len(array)
    for i in range (0,n-1):
        flag =False
        for j in range(0,n-1-i):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]
                flag=True
        if not flag:
            break
    return array
def SelectionSort(array):
    n=len(array)
    for i in range(0,n-1):
        mini=i
        for j in range(i+1,n):
            if(array[j]<array[mini]):
                mini=j    
        array[mini],array[i]=array[i],array[mini]
    return array
def MergeSort(array,start,end):
   if start < end:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end) 
def Merge(array,p,q,r):
    left = array[p:q+1]
    right = array[q+1:r+1]
    i=j=0
    k=p
    while(i<len(left) and j<len(right)):
        if(left[i]<=right[j]):
            array[k]=left[i]
            i=i+1
        else:
            array[k]=right[j]
            j=j+1
        k=k+1
    while(i<len(left)):
        array[k]=left[i]
        i=i+1
        k=k+1
    while(j<len(right)):
        array[k]=right[j]
        j=j+1
        k=k+1
def CountSort(array):
    maximum=max(array)     
    count_arr=[0]*(maximum+1)
    output_arr=[0]*(len(array))
    for i in range (0,len(array)):
        count_arr[array[i]]+=1
    for i in range(0,len(count_arr)):
        if i !=0:
            count_arr[i]=count_arr[i]+count_arr[i-1]
    i=len(array)-1
    while i>=0:
        index=count_arr[array[i]]-1
        count_arr[array[i]]-=1
        output_arr[index]=array[i]
        i-=1
    for i in range(len(array)):
        array[i]=output_arr[i]
def RadixSort(array):
    maximum = max(array)
    place = 1
    while maximum // place > 0:
        CountSortForRadix(array, place)
        place *= 10
def CountSortForRadix(array, place):
    count_arr = [0] * 10
    output_arr = [0] * len(array)
    
    for i in range(len(array)):
        index = array[i] // place
        count_arr[index % 10] += 1
    
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    
    i = len(array) - 1
    while i >= 0:
        index = array[i] // place
        output_arr[count_arr[index % 10] - 1] = array[i]
        count_arr[index % 10] -= 1
        i -= 1
    
    for i in range(len(array)):
        array[i] = output_arr[i]
def QuickSort(array,start,end):
    if start<end:
        q=Partition(array,start,end)
        QuickSort(array,start,q-1)
        QuickSort(array,q+1,end)   
def Partition(array,start,end):
    Pivot=array[end]
    i=start-1
    j=start
    for j in range(start ,end):
        if(array[j]<=Pivot):
            i+=1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[end]=array[end],array[i+1]
    return i+1
def BucketSort(array):
    n=len(array)
    Bucket=[[] for _ in range(n)]
    sortedArray=[]
    for i in range(n):
        index=int(n*array[i])
        Bucket[index].append(array[i])
    for i in range(n):
       Bucket[i]= InsertionSort(Bucket[i])
    for i in range(n):
        sortedArray.extend(Bucket[i])
    return sortedArray      
