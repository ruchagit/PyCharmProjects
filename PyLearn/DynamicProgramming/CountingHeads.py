def counting_heads(p,k,i,res,ret):
    if i == len(p):
        return res if k == 0 else 0

    val1 = counting_heads(p, k, i+1, res* (1-p[i]), ret)
    ret1 = []
    ret1.extend(ret)
    ret1.append(i)
    val2 = counting_heads(p, k-1, i+1, res * p[i], ret1)
    if val2 > val1:
        max_val = val2
        while len(ret)>0:
            ret.pop(0)
        ret.extend(ret1)
    else:
        max_val = val1
    return max_val


def counting_heads_dp(p,k):
    n = len(p)
    dp = [[0 for x in range(k+1)] for x in range(n)]
    dp[0][0] = 1-p[0]
    dp[0][1] = p[0]
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] * (1-p[i])
    for r in range(1,n):
        for c in range(1,k+1):
            dp[r][c] = max(dp[r-1][c] * (1-p[r]), dp[r-1][c-1] * p[r])
    return dp


def string_break(n, m):
    h = len(m)+2
    L = [0] * h
    for i in range(0, len(m)):
        L[i+1] = m[i]
    L[len(L)-1] = n
    print L
    dp = [[float('inf') for x in range(h)] for x in range(h)]
    for i in range(0,h):
        dp[i][i] = 0
        if i+1 < h:
            dp[i][i+1] = 0
    for l in range(3, h+1):
        for i in range(0, h-l+1):
            j = i+l-1
            min_val = float('inf')
            for k in range(i+1, j):
                min_val = min(min_val, dp[i][k] + dp[k][j])
            dp[i][j] = L[j] - L[i] + min_val
    return dp

def select_cards(v):
    n = len(v)
    dp = [[[] for x in range(n)] for x in range(n)]
    for i in range(n):
        dp[i][i] = [v[i],0,v[i]]
    for l in range(2,n+1):
        for i in range(0,n-l+1):
            j = i+l-1
            left_val = v[i] + dp[i+1][j][1]
            right_val = v[j] + dp[i][j-1][1]
            if left_val >= right_val:
                dp[i][j].insert(0, left_val)
                dp[i][j].insert(1, dp[i+1][j][0])
                dp[i][j].append(v[i])
            else:
                dp[i][j].insert(0, right_val)
                dp[i][j].insert(1, dp[i][j-1][0])
                dp[i][j].append(v[j])
    return dp

def change_coins_recursive(x, i, V):
    if i == len(x):
        if V==0:
            return True
        else:
            return False
    val1 = change_coins_recursive(x, i + 1, V)
    if x[i] <= V:
        val2 = change_coins_recursive(x, i + 1, V - x[i])
    else:
        val2 = False
    return val1 or val2

def change_coins_dp(x, V):
    n = len(x)
    dp = [[False for g in range(V+1)] for g in range(n)]
    for i in range(n):
        dp[i][0] = True
    for i in range(n):
        for j in range(V+1):
            val1 = dp[i-1][j]
            if x[i] <= j:
                val2 = dp[i-1][j-x[i]]
            else:
                val2 = False
            dp[i][j] = val1 or val2
    return dp[n-1][V]

def inf_change_coins_k(x, V, initk , k):
    if k == 0:
        if V > 0:
            return False
        else:
            return True
    if V <= 0:
        if k <= initk:
            return True
        else:
            return False
    maxval = False
    for i in range(len(x)):
        if x[i] <= V:
            val = inf_change_coins_k(x, V-x[i], initk, k-1)
            maxval = maxval or val
    return maxval


def dp_change_coins_k(x, V, k):
    dp = [float('inf')]*(V+1)
    dp[0] = 0
    for v in range(V+1):
        for i in range(len(x)):
            if x[i] <= v:
                if dp[v-x[i]]+1 < dp[v]:
                    dp[v] = dp[v-x[i]]+1
    return dp[V] <= k

def dp_subset_sum(a, S):
    dp = [[False for i in range(S+1)] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(S+1):
            if dp[i][j] == j:
                dp[i][j] = True
            elif a[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-a[i]] or dp[i-1][j]
    return dp[len(a)-1][S]

def dp_world_series(n,i,j):
    x = n-i
    y = n-j
    dp = [[0 for g in range(x+1)] for g in range(y+1)]
    for g in range(1, y+1):
        dp[g][0] = 1
    for r in range(1, y+1):
        for c in range(1, x+1):
            dp[r][c] = 0.5 * (dp[r-1][c] + dp[r][c-1])
    return dp[y][x]

if __name__ == '__main__':
    p = [0.1, 0.2, 0.3]
    ret = []
    # print counting_heads(p, 2, 0, 1, ret)
    # print ret
    # print counting_heads_dp(p,2)
    dp = string_break(9,[2,5,8])
    for i in range(len(dp)):
        print dp[i]
    # print mm
    # print formation
    # v = [3,9,1,2]
    # res =  select_cards(v)
    # for i in range(len(res)):
    #     print res[i]
    # print change_coins_dp([1, 5, 10, 20], 40)
    # print dp_change_coins_k([5,10], 55, 6)
    # print dp_subset_sum([6,9,1,5,4], 8)
    # print dp_world_series(8, 2, 6)