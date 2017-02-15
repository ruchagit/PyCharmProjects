def sortCharacters(inString):
    s = [x for x in inString]
    quicksort(s,0,len(s)-1)
    return ''.join(str(x) for x in s)


def quicksort(a,start,end):
    if start < end:
        pivot_idx = partition(a, start, end)
        quicksort(a, start, (pivot_idx-1))
        quicksort(a, (pivot_idx+1), end)


def partition(a,start,end):
    p = a[start]
    lt = start+1
    rt = end
    while rt > lt:
        while a[lt] <= p and lt < end:
            lt += 1
        while a[rt] > p and rt > start:
            rt -= 1
        if rt > lt:
            a[rt], a[lt] = a[lt], a[rt]
    if a[start] > a[rt]:
        a[start], a[rt] = a[rt], a[start]
    return rt

if __name__ == '__main__':
    _inString = str('This is easy')
    res = sortCharacters(_inString)
    print(res)