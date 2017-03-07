def matrix_paths(i, j, m, n, a, memo):
    mod = 1000000007
    if (i,j) in memo:
        return memo[(i,j)]
    if i == m or j == n:
        return 0
    if a[i][j] == 0:
        return 0
    if i == m-1 and j == n-1:
        return 1
    memo[(i,j)] = (matrix_paths(i+1, j, m, n, a,memo) \
                  + matrix_paths(i, j+1, m, n, a, memo) + mod) % mod
    return memo[(i,j)]

def matrix_paths_dp(a):
    mod = 1000000007
    rows = len(a)
    cols = len(a[0])
    dp = [[0 for x in range(cols)] for x in range(rows)]
    dp[rows-1][cols-1] = 1
    for r in range(rows-1, -1, -1):
        for c in range(cols-1, -1, -1):
            if a[r][c] == 0:
                continue
            if r + 1 < rows :
                dp[r][c] = (dp[r][c] + dp[r+1][c] + mod) % mod
            if c + 1 < cols:
                dp[r][c] = (dp[r][c] + dp[r][c+1] + mod) % mod
    return dp[0][0]

if __name__ == '__main__':
    a = [[1 for x in range(4)] for x in range(3)]
    # print matrix_paths(0,0,2,2,a,dict())
    print matrix_paths_dp(a)