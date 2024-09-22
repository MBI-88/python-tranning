

def freq_count(arry:[], obj:int) -> dict[int]:
    freq:dict[int] = {}
    level  = -1
    strArray = str(arry)
    strArray = list(strArray)

    for i in strArray:
        if i == "[":
            level += 1
            freq[level] = 0 

    level = -1 
    for ar in strArray:
        if ar == "[":
            level += 1
        elif ar == "]":
            level -= 1 
        
        if ar == str(obj):
            freq[level] += 1

    return freq




if __name__ == "__main__":
    print(freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1))
    print(freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5))
    print(freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2))