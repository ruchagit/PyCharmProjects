def recursiveLCS(a,b,n,m):
    if n == -1 or m == -1:
        return 0
    if a[n] == b[m]:
        return 1 + recursiveLCS(a,b,n-1,m-1)
    else:
        return max(recursiveLCS(a,b,n-1,m), recursiveLCS(a,b,n,m-1))

def recursiveLCS_returnresult(a,b,n,m,res):
    if n == len(a) or m == len(b):
        return 0
    if a[n] == b[m]:
        res.append(a[n])
        return 1 + recursiveLCS_returnresult(a,b,n+1,m+1,res)
    else:
        res1 = []
        res2 = []
        l1 = recursiveLCS_returnresult(a,b,n+1,m,res1)
        l2 = recursiveLCS_returnresult(a,b,n,m+1,res2)
        if l1 > l2:
            res.extend(res1)
            return l1
        else:
            res.extend(res2)
            return l2

def recursiveLCS_bottomup(a,b,n,m):
    res = [[0 for x in range(n+1)] for y in range(m+1)]
    for x in range(1, n+1):
        for y in range(1, m+1):
            if a[x-1] == b[y-1]:
                res[x][y] = res[x-1][y-1] + 1
            else:
                res[x][y] = max(res[x-1][y], res[x][y-1])
    return findLCS(a,b,res,n,m)

def findLCS(a,b,res,n,m):
    lcs = []
    while n>=0 and m>=0:
        if a[n-1] == b[m-1]:
            lcs.append(a[n-1])
            n -= 1
            m -= 1
        else:
            if res[n-1][m] < res[n][m-1]:
                m -= 1
            else:
                n -= 1
    return lcs

def recursiveLCS_memo(a,b,n,m,map):
    if n == len(a) or m == len(b):
        return [0]
    if (n,m) in map:
        return map[(n,m)]
    if a[n] == b[m]:
        val = recursiveLCS_memo(a,b,n+1,m+1,map)
        map[(n,m)] = [1 + val[0]]
        map[(n,m)].append(a[n])
        map[(n,m)].extend(val[1:])
        return map[(n, m)]
    else:
        val1 = recursiveLCS_memo(a,b,n+1,m,map)
        val2 = recursiveLCS_memo(a,b,n,m+1,map)
        new = []
        if val1[0] > val2[0]:
            # new.extend(val1)
            map[(n,m)] = val1
        else:
            # new.extend(val2)
            map[(n, m)] = val2
        # map[(n, m)] = new
        return map[(n, m)]

def recursiveLCS_memo1(a,b,n,m,map):
    if n == len(a) or m == len(b):
        return 0
    if (n,m) in map:
        return map[(n,m)]
    if a[n] == b[m]:
        val = recursiveLCS_memo1(a,b,n+1,m+1,map)
        map[(n,m)] = 1 + val
        return map[(n, m)]
    else:
        val1 = recursiveLCS_memo1(a,b,n+1,m,map)
        val2 = recursiveLCS_memo1(a,b,n,m+1,map)
        if val1 > val2:
            map[(n, m)] = val1
        else:
            map[(n, m)] = val2
        return map[(n, m)]

if __name__ == '__main__':
    # print recursiveLCS([1,3,2,7,8], [3,1,2,7,8], 4, 4)
    # res = []
    # recursiveLCS_returnresult([1, 7, 3, 2, 8], [3, 1, 2, 7, 8], 0, 0,res)
    # print res
    # print recursiveLCS_bottomup([1,3,2,7,8], [3,1,2,7,8], 5, 5)
    map = dict()
    recursiveLCS_memo([1, 0, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 0, 1, 1, 0], 0, 0, map)
    print map[(0,0)]