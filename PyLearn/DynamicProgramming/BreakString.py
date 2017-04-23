def breakString(m, S, i,d):
    if i == len(m):
        return 0
    mincost = float('inf')
    print m[i]
    for k in range(0,len(m)):
        cost = S + breakString(m, S - m[k], i+1)
        if cost < mincost:
            mincost = cost
    return mincost


def allPerms(m, k):
    if k == len(m):
        print  m
        return
    for i in range(k, len(m)):
        swap(m, k, i)
        allPerms(m, k+1)
        swap(m, k, i)

def swap(a,i,j):
    a[i],a[j] = a[j], a[i]

if __name__ == '__main__':
    m = [1, 2, 3]
    S = 9
    # print breakString(m, S, 0)
    print allPerms(m, 0)