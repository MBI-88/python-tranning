


def sortfrequency(string:str) -> str:
    array = [i for i in string]
   
    for i in range(len(array)):
        j = i + 1
        while (j < len(array)):
            if abs(ord(array[i]) - ord(array[j])) >= 30: # lowercase
                if array[i] > array[j]:
                    pass
                else:
                    array[i], array[j] = array[j],array[i]

            else:
                if array[i] > array[j]:
                    array[j], array[i] = array[i], array[j]
           
            
            j += 1
    
    return "".join(array)
        
