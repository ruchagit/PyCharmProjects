def obst(nodes, cost):
    n = len(nodes)
    dp = [[[0,-1] for x in range(n)] for x in range(n)]
    for i in range(n):
        dp[i][i][0] = cost[i]
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            minval = float('inf')
            val = 0
            for k in range(i, j):
                val += cost[k]
                if dp[i][k-1][0] + dp[k+1][j][0] < minval:
                    minval = dp[i][k-1][0] + dp[k+1][j][0]
                    node = k
            if dp[i][j-1][0] < minval:
                minval = dp[i][j-1][0]
                node = j
            val += cost[j]
            dp[i][j] = [val + minval, node]
    return dp

if __name__ == '__main__':
    nodes = [10,12,16,21]
    cost = [4,2,6,3]
    print obst(nodes,cost)