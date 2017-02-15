def mergearrays(iarray):
    l = len(iarray)
    if l == 0:
        return iarray
    elif l == 1:
        return iarray[0]
    elif l == 2:
        return merge_two_arrays(iarray[0], iarray[1])
    else:
        return merge_two_arrays(mergearrays(iarray[0:l//2]),
                                mergearrays(iarray[l//2:l]))

def merge_two_arrays(a1,a2):
    l = len(a1)
    for i in range(l-1):
        if a1[i] < a1[i+1] or a2[i] < a2[i+1]:
            a1 = merge_two_arrays_asc(a1, a2)
            return a1
        elif a1[i] > a1[i+1] or a2[i] > a2[i+1]:
            a1 = merge_two_arrays_desc(a1, a2)
            return a1
    a1 = merge_two_arrays_asc(a1, a2)
    return a1

def merge_two_arrays_asc(a1, a2):
    i = len(a1) - 1
    j = len(a2) - 1
    k = i + j + 1
    res = [None] * (k + 1)
    while k >= 0:
        if j < 0 or (i >= 0 and a1[i] > a2[j]):
            res[k] = a1[i]
            k -= 1
            i -= 1
        else:
            res[k] = a2[j]
            k -= 1
            j -= 1
    return res

def merge_two_arrays_desc(a1, a2):
    i = len(a1) - 1
    j = len(a2) - 1
    k = i + j + 1
    res = [None] * (k + 1)
    while k >= 0:
        if j < 0 or (i >= 0 and a1[i] < a2[j]):
            res[k] = a1[i]
            k -= 1
            i -= 1
        else:
            res[k] = a2[j]
            k -= 1
            j -= 1
    return res

if __name__ == '__main__':
    #iarray = [[1, 1, 1], [2, 3, 4]]
    #iarray = [[1], [2]]
    #iarray = [[5,8, 11], [1, 1, 1], [2, 3, 4]]
    #iarray = [[11, 8, 1], [1, 0, -10], [22, 3, -19]]
    iarray = [[1, 1, 1], [2, -1, -4]]
    res = mergearrays(iarray)
    print(res)