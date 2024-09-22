def findPattern(pattern:str, frame:str) -> str:
    l, r, count = 0,0,0
    minWindow = len(frame) * 2
    mapper = dict[str:int]()
    result = ""
    if len(pattern) > len(frame): return ""

    for i in pattern:
        mapper[i] = 0
    for i in pattern:
        mapper[i] += 1

    while r < len(frame):
        if frame[r] in mapper:
            mapper[frame[r]] -= 1
            if mapper[frame[r]] >= 0: count += 1
        
        while count == len(pattern):
            if frame[l] in mapper:
                if r - l + 1 < minWindow:
                    minWindow = r - l + 1
                    result = frame[l : r + 1]

                mapper[frame[l]] += 1
                if mapper[frame[l]] > 0: count -= 1

            l += 1

        r += 1
    return result