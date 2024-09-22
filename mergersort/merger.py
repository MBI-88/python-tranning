def merger(left:[], right:[]) -> object:
    l = 0
    r = 0
    result = []

    while (l < len(left) and r < len(right)):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    while (l < len(left)):
        result.append(left[l])
        l += 1
    
    while (r < len(right)):
        result.append(right[r])
        r += 1
    
    return result


def mergersort(array:[]) -> object:
    if len(array) < 2: 
        return array
    left = mergersort(array[:len(array) // 2])
    right = mergersort(array[len(array) // 2 :])
    return merger(left, right)