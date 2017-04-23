import heapq
from random import randint
import random

def topK(iStream, iK):
    minheap = [None] * (iK+1)
    minheap = build_min_heap(minheap, iStream[0:iK])
    print (minheap)
    for i in range(iK, len(iStream)):
        if iStream[i] > minheap[1]:
            minheap[1] = iStream[i]
            sink_down(minheap, 1)
            print(minheap)
    return minheap[1:]


def build_min_heap(mh,arr):
    pos = 0
    for i in range(len(arr)):
        if pos == 0:
            mh[1] = arr[i]
            pos += 2
        else:
            mh[pos] = arr[i]
            mh = bubble_up(pos, mh)
            pos += 1
    return mh


def bubble_up(p,mh):
    while p > 0 and mh[p//2] is not None and mh[p//2] > mh[p]:
        mh[p//2], mh[p] = mh[p], mh[p//2]
        p //= 2
    return mh


def sink_down(mh, k):
    pos = len(mh)-1
    smallest = k
    if k*2 <= pos and mh[k*2] < mh[smallest]:
        smallest = k*2
    if k*2+1 <= pos and mh[k*2+1] < mh[smallest]:
        smallest = k*2+1
    if smallest != k:
        mh[k], mh[smallest] = mh[smallest], mh[k]
        sink_down(mh, smallest)

'''
Nearest neighbours
'''


def nearest_neighbours(pArr, k, p):
    n = len(pArr)
    dist = [None] * n
    kClosest = [None] * (k)
    k_copy = k
    j = 0
    for i in range(n):
        dist[i] = get_distance(p, pArr[i])
    print(dist)
    kth = kPartition(dist, 0, n-1, k)
    print("kth :", kth)
    while j < n and k_copy >= 0:
        if get_distance(p, pArr[j]) <= kth:
            kClosest[k_copy] = pArr[j]
        j += 1
        k_copy -= 1
    return kClosest


def get_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)


def kPartition(dArr, start, end, k):
    if start < end:
        pivot = partition(dArr, start, end)
        print("pivot :",pivot)
        x = pivot - start + 1
        if k == x:
            print ('equal to : ', dArr, dArr[pivot])
            return dArr[pivot]
        elif k < x:
            print ('smaller than')
            kPartition(dArr, start, pivot - 1, k)
        else:
            print ('greater than')
            kPartition(dArr, pivot + 1, end, k)


def partition(dArr, start, end):
    i = int(round(start + random.random() * (end-start)))
    print("i :",i)
    dArr[end], dArr[i] = dArr[i], dArr[end]
    print("before:", dArr)
    pivot_element = dArr[end]
    lt = start
    rt = start
    while rt < end:
        if dArr[rt] <= pivot_element:
            dArr[lt], dArr[rt] = dArr[rt], dArr[lt]
            lt += 1
            rt += 1
        else:
            rt += 1
    dArr[lt], dArr[end] = dArr[end], dArr[lt]
    print("after:", dArr)
    return lt


def subsets(idx, list, result, counter):
    print counter[0]
    if idx < len(list):
        n = len(result)
        c = list[idx]
        for i in xrange(n):
            result.append(result[i]+[c])
            counter[0] += 1
        subsets(idx + 1, list,result,counter)





if __name__ == '__main__':
    #iStream = [1, 23, 12, 9, 30, 2, 50]
    #iK = 2
    r = [[]]
    c = {}
    c[0] =  1
    subsets(0,[1,2,3,4,5],r, c)
    print c[0], r

    #iStream = [(4, 3), (1, 1), (0, 0), (2, 1), (2, 2), (5, 5)]
    iK = 4
    p = (0,0)
    #res = topK(iStream, iK)
    #res = nearest_neighbours(iStream, iK, p)
    #print(res)
