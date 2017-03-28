def pal(s):
    sl = len(s)
    dp = [[0 for x in range(sl)] for x in range(sl)]
    for l in range(2,sl+1):
        for i in range(sl-l+1):
            j = i+l-1
            if is_palindrome(s,i,j):
                dp[i][j] = 0
            else:
                val = float('inf')
                for k in range(i,j):
                    val = min(val, dp[i][k] + dp[k+1][j] + 1)
                dp[i][j] = val
    print dp
    return dp[0][sl-1]

def is_palindrome(s,i,j):
    while j>i:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    s = "abcbm"
    print pal(s)