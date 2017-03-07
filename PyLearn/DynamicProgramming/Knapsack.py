def knapsack_recurssion(w, v, n, W):
    if n == -1 or W <= 0:
        return 0
    maxval = knapsack_recurssion(w,v,n-1,W)
    if w[n] <= W:
        maxval = max(maxval,
                     knapsack_recurssion(w,v,n-1,W-w[n]) + v[n])
    return maxval

def knapsack_recurssion_items(w, v, n, W,items):
    if n == -1 or W <= 0:
        return 0
    maxval = knapsack_recurssion_items(w,v,n-1,W,items)
    if w[n] <= W:
        max1 = maxval
        max2 = knapsack_recurssion_items(w,v,n-1,W-w[n],items) + v[n]
        if max2 > max1:
            maxval = max2
            if w[n] not in items:
                items.append(w[n])
        else:
            if w[n] in items:
                items.remove(w[n])
    else:
        if w[n] in items:
            items.remove(w[n])
    print items
    return maxval

def knapsack_dp(w, v, n, W):
    arr = {}
    arr[0] = [0]
    for i in range(1,W+1):
        m = 0
        for j in range(len(w)):
            p = i - w[j]
            #print i,j,p,arr
            if p in arr and (arr[p][0] + v[j] >= m) and \
                            w[j] not in arr[p][1:]:
                m = arr[p][0] + v[j]
                arr[i] = [m]
                arr[i].extend(arr[p][1:])
                arr[i].append(w[j])
    return arr


def inf_knapsack_recurssion(w, v, W,items):
    # if W <= 0:
    #     return 0
    # #dont need the base case separately since maxval = 0 covers it
    maxval = 0
    for i in range(len(v)):
        if w[i] <= W:
            val = inf_knapsack_recurssion(w,v,W-w[i],items)+v[i]
            if val >= maxval:
                maxval = val
                items.append(w[i])
    return maxval

def inf_knapsack_dp(w,v,W):
    #dp = [0]*(W+1)
    dp = {}
    dp[0] = [0]
    for capacity in range(1, W+1):
        maxval = 0
        for i in range(len(w)):
            if w[i] <= capacity:
                if capacity - w[i] in dp:
                    if dp[capacity - w[i]][0] + v[i] >= maxval:
                        maxval = dp[capacity - w[i]][0] + v[i]
                        dp[capacity] = [maxval]
                        dp[capacity].extend(dp[capacity - w[i]][1:])
                        dp[capacity].append(w[i])
    return dp

def inf_knapsack_dp2(w,v,W):
    dp = [0]*(W+1)
    for capacity in range(1, W+1):
        for i in range(len(w)):
            if w[i] <= capacity and dp[capacity - w[i]]+v[i] >= dp[capacity]:
                dp[capacity] = dp[capacity-w[i]] + v[i]
    return dp


if __name__ == '__main__':
    w = [1,3,4,5]
    v = [1,6,5,7]
    W = 3
    items = []
    # print inf_knapsack_recurssion(w,v,W,items)
    # print items
    print inf_knapsack_dp2(w, v, W)
    #print knapsack_dp(w,v,3,W)
    # print knapsack_recurssion_items(w,v,4,W,items)
    # print items