
def bubblesort(array: []) -> object:
    if len(array) == 0: return array 

    for i in range(len(array)):
        j = i + 1
        while (j < len(array)):
            if array[i] > array[j]:
                array[j], array[i] = array[i], array[j]
            
            j += 1
    
    return array 