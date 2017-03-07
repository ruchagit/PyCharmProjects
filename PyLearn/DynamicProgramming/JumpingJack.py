def jumping_jack(n,k):
    # return jumping_jack_recur(0,1,n,k)
    memo = dict()
    return jumping_jack_memo(0,1,n,k,memo)

def jumping_jack_recur(i,j,n,k):
    if i == k:
        return float('-inf')
    if j == n+1:
        return i
    val1 = jumping_jack_recur(i,j+1,n,k)
    val2 = jumping_jack_recur(i+j,j+1,n,k)
    return max(val1,val2)

def jumping_jack_memo(i,j,n,k,memo):
    if i == k:
        return float('-inf')
    if j == n+1:
        return i
    if (i,j) in memo:
        return memo[(i,j)]
    val1 = jumping_jack_memo(i, j+1, n, k, memo)
    val2 = jumping_jack_memo(i+j, j+1, n, k, memo)
    memo[(i,j)] = max(val1, val2)
    return memo[(i,j)]

def step(n,k):
    T = [0] * (n+1)
    T[0] = 0
    for i in range(1,n+1):
        T[i] = T[i-1]
        for j in range(i):
            c = T[j] + i
            if c != k:
                T[i] = max(T[i], c)
    return T

def step1(n,k):
    pos = 0
    for i in range(1,n+1):
        pos += i
        if pos == k:
            pos -= 1
    return pos


if __name__ == '__main__':
    print step1(3,3)