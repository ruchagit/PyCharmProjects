def calcF(M):
    F = []
    F.append(1)
    F.append(1)
    for i in range(2, M+1):
        add = 0
        for k in range(4,0,-1):
            if i-k >= 0:
                add += F[i-k]
        F.append(add)
    return F


def calcG(F,N):
    mod = 1000000007
    G = [[0 for x in range(len(F))] for x in range(N+1)]
    for i in range(len(F)):
        G[0][i] = 0
        G[1][i] = F[i]
    for i in range(2, N+1):
        for j in range(len(F)):
            G[i][j] = G[i-1][j] * F[j] % mod
    return G


def my_pow(base, exp):
    mod = 1000000007
    res = 1
    while exp:
        if exp % 2:
            res = res * base % mod
        base = base * base % mod
        exp /= 2
    return res


def calcH(G,M):
    mod = 1000000007
    H = [0] * (M+1)
    H[0] = 1
    H[1] = 1
    for i in range(2, M+1):
        t = 0
        for j in range(1, i):
            t += H[j] * G[i-j] % mod
        H[i] = (G[i] - t + mod) % mod
    return H[M]


if __name__ == '__main__':
    n = int(raw_input())
    tests = []
    maxN = 0
    maxM = 0
    for i in range(n):
        N, M = raw_input().split(' ')
        N = int(N)
        M = int(M)
        tests.append((N,M))
        maxN = max(N,maxN)
        maxM = max(M,maxM)
    F = calcF(maxM)
    G = calcG(F, maxN)
    for k in range(n):
        print calcH(G[tests[k][0]], tests[k][1])
