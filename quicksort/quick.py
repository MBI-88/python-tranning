

def partitioner(array:[], low:int, high:int) -> ([],int):
    pivote = array[high]
    p = low 
    i = low
    while (i < high):
        if array[i] < pivote:
            array[p],array[i] = array[i], array[p]
            p += 1
        
        i += 1
    
    array[p],array[high] = array[high], array[p]
    return array, p


def quicksort(data:[], low:int, high:int) -> object:
    if low < high:
        arr , p = partitioner(data, low, high)
        data = quicksort(arr, low, p-1)
        data = quicksort(arr, p + 1, high)
    return data