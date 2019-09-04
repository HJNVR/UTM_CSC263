# Quicksort is a Divide and conquer algorithm. It picks an element as pivot and
# partitions the given array around the picked pivot. 会选择一个数当作pivot

#一共有三种方法选择pivot
#[1] always pick first element as pivot
#[2] always pick last element as pivot
#[3] pick a random element as pivot
#[4] pick median as pivot

def partition(arr,low,high):
    """
    选择最后一个element作为pivot
    array最后会变成最大的数字在最右边， 但并不完全是一个sorted array
    >>> arr = [2,1,3,5,6]
    >> partition(arr,0,4)
    4
    >> arr = [2,1,3,5,6]
    >>> arr = [6,1,2,3]
    >>> partition(arr,0,3)
    >>> arr = [3,1,2,6]
    """
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    #print(arr)  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )

def quickSort(arr,low,high):
    """
    >>> arr = [2,1,3,5,6]
    >>> quickSort(arr,0,4)
    >>> arr
    [1,2,3,5,6]
    """
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) # 得到array的partition index
  
        # Separately sort elements before 
        # partition and after partition  
        quickSort(arr, low, pi-1) # 然后分别sort partition的左边和右边
        quickSort(arr, pi+1, high)
