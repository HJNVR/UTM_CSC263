def heapify(arr, n ,i):
    """ build max heap this function works as "Bubble down"
    >>>arr = [18,33,25,65,24,40]
    >>>heapify(arr,6,0)
    >>>arr
    [60,40,25,33,18,24]
    """
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
        heapify(arr, n, largest)

def BuildMaxHeap(arr):
    # these functions in this file convert a unsotred arry to a max-heap array
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr,n,i)
    #print(arr)

def print_arr(arr):
    result = []
    for i in range(len(arr)):
        result.append(arr[i])
    return result

def HeapSort(arr):
    """
    this function makes the max-heap array into ta sorted array
    >>>arr = [18,33,25,65,24,40]
    >>>BuildMaxHeap(arr)
    >>>arr
    [65, 33, 40, 18, 24, 25]
    >>>HeapSort(arr)
    [18,33,25,65,24,40]
    """
    n = len(arr)
    BuildMaxHeap(arr)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i] # swap
        heapify(arr, i, 0)








    
