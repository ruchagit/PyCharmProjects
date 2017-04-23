def problem4(g,u,v):
    dist = dict()
    dist[u] = (0,[u])
    bfs(g,u,v,dist)
    return dist

def bfs(g,u,v,dist):
    q = [u]
    while q:
        e = q.pop(0)
        nextd = dist[e][0] + 1
        for i in g[e]:
            if i not in dist:
                dist[i] = (nextd,[e])
                q.append(i)
            else:
                if dist[i][0] == nextd:
                    dist[i][1].append(e)



if __name__ == '__main__':
    # g = {0:[1],1:[0,2,4],2:[1,3],3:[2,4,5],4:[1,3,5],5:[3,4]}
    g = {0: [], 1: [2,3], 2: [1,4,5], 3: [1,8,6], 4: [2,5,7],
         5: [2,7], 6:[3,7,8], 7:[4,5,6], 8:[3,6]}
    print problem4(g,1,7)



# {1: (0, [1]),
#  2: (1, [1]),
#  3: (1, [1]),
#  4: (2, [2]),
#  5: (2, [2]),
#  6: (2, [3]),
#  7: (3, [4, 5, 6]),
#  8: (2, [3])}
