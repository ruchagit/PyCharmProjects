def maxSubArray(arr):
    curr_max = arr[0]
    max_sum = arr[0]
    start = 0
    end = 0
    for i in range(1,len(arr)):
        if curr_max + arr[i] > arr[i]:
            curr_max = curr_max + arr[i]
            end = i
        else:
            curr_max = arr[i]
            start = i
            end = i
        max_sum = max(max_sum,curr_max)
    return [start,end,max_sum]

if __name__ == '__main__':
    print maxSubArray([5,15,-30,10,-5,40,10])