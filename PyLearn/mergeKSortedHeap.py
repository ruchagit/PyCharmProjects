class HeapNode:
    def __init__(self,val,i,j):
        self.val = val
        self.i = i
        self.j = j


def mergeKSorted(lists):
    k = len(lists)
    n = len(lists[0])
    heap = [HeapNode]
    res = []
    for i in range(k):
        node = HeapNode(lists[i][0],i,0)
        heap.append(node)
    buildHeap(heap,k)
    #printHeap(heap,k)
    while heap:
        res.append(getMin(heap))
        deleteMin(heap)


def printHeap(heap,k):
    for i in range(1,k+1):
        print heap[i].val,


def getMin(heap):
    return heap[1].val


def buildHeap(heap,k):
    for i in range(k/2, 0, -1):
        heapify(heap,i,2*i,2*i+1,k)

def heapify(heap,p,lc,rc,k):
    smallest = p
    if lc <=k and heap[lc].val < heap[p].val:
        smallest = lc
    if rc <=k and heap[rc].val < heap[smallest].val:
        smallest = rc
    if smallest != p:
        heap[p],heap[smallest] = heap[smallest], heap[p]
        heapify(heap,smallest,2*smallest,2*smallest+1,k)

def infiniteArray(arr,k):
    if len(arr) == 0:
        return -1
    if arr[0] == k:
        return 0
    if arr[1] == k:
        return 1
    return helper(arr, 2**1, 2**2, k)

def helper(arr,prev_index,curr_index,k):
    if arr[curr_index] > k:
        return binarySearch(arr,prev_index,curr_index,k)
    elif arr[curr_index] < k:
        prev_index = curr_index
        curr_index *= 2
        return helper(arr,prev_index,curr_index,k)

def binarySearch(arr,start,end,k):
    mid = (start+end) //2
    if arr[mid] < k:
        return binarySearch(arr,mid+1,end,k)
    elif arr[mid] > k:
        return binarySearch(arr,start,mid-1,k)
    else:
        return mid

#in a sorted array of distinct numbers, find i such that a[i] = i
# O(log n)
def findNumAsIndex(a,start,end):
    if start == end:
        return (start,a[start] == start)
    mid = (start+end) // 2
    if a[mid] - mid == 0:
        return (mid, True)
    elif a[mid] - mid > 0:
        return findNumAsIndex(a,start,mid-1)
    else:
        return findNumAsIndex(a,mid+1,end)



if __name__ == '__main__':
    #lists = [5,6,10],[7,11,13],[1,2,9],[0,3,4]
    #mergeKSorted(lists)
    #print infiniteArray([1,2,3,4,5,6,7,8,9,10,11,12,-99,-99,-99,-99],3)
    # print findNumAsIndex([0,2,4,7],0,5)
    print binarySearch([1,2,3,4,5],0,5,4)