import math
def makeSegmentTree(arr, l):
    # power of 2
    if l > 0 and ((l & (l-1)) == 0):
        seg = [None] * (l*2-1)
    # find the next closest power of 2
    else:
        next_power = int(math.pow(2,math.ceil(math.log(l,2))))
        seg = [None] * (next_power*2-1)
    makeSegmentTreeHelper(arr, seg, 0, l-1, 0)
    return seg


def makeSegmentTreeHelper(arr, seg, low, high, pos):
    if low == high:
        seg[pos] = arr[low]
        return
    mid = (low + high) // 2
    makeSegmentTreeHelper(arr, seg, low, mid, pos*2+1)
    makeSegmentTreeHelper(arr, seg, mid+1, high, pos*2+2)
    seg[pos] = min(seg[pos*2+1], seg[pos*2+2])


def rangeMinQuery(seg, qlow, qhigh, low, high, pos):
    # total overlap
    if qlow <= low and qhigh >= high:
        return seg[pos]
    # no overlap
    elif qlow > high or qhigh < low:
        return float('inf')
    mid = (low + high) // 2
    return min(rangeMinQuery(seg, qlow, qhigh, low, mid, pos*2+1),
               rangeMinQuery(seg, qlow, qhigh, mid+1, high, pos*2+2))


if __name__ == '__main__':
    arr = [-1, 2, 4, 0]
    l = len(arr)
    seg = makeSegmentTree(arr, l)
    res = rangeMinQuery(seg, 0, 3, 0, l-1, 0)
    print res
