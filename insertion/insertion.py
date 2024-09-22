def insertionsort(data:[]) -> object:
    if len(data) == 0 : return data
    i = 0
    j = 0
    while (i < len(data)):
        j = i
        while (j > 0 and data[j - 1] > data[j]):
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1

        i += 1
    
    return data