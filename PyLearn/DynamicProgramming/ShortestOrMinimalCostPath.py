def minimal_cost(mat):
    rows = len(mat)
    cols = len(mat[0])
    dp = [[0 for x in range(cols)] for x in range(rows)]
    dp[0][0] = mat[0][0]
    for c in range(1,cols):
        dp[0][c] = mat[0][c] + dp[0][c-1]
    for r in range(1,rows):
        dp[r][0] = mat[r][0] + dp[r-1][0]
    for r in range(1,rows):
        for c in range(1,cols):
            cost = mat[r][c]
            dp[r][c] = min((dp[r-1][c] + cost),
                           (dp[r][c-1] + cost))
    return dp

def get_route(dp, mat):
    r = len(mat)-1
    c = len(mat[0])-1
    res = [(r,c)]
    while r>0 and c>0:
        f = dp[r][c] - mat[r][c]
        prev_p = (r-1,c) if f == dp[r-1][c] else (r,c-1)
        res.insert(0,prev_p)
        r = prev_p[0]
        c = prev_p[1]
    res.insert(0,(0,0))
    return res


if __name__ == '__main__':
    mat = [[1,3,5,8],
           [4,2,1,7],
           [4,3,2,3]]
    dp = minimal_cost(mat)
    print get_route(dp,mat)