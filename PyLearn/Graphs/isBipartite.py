def is_bipartite(g,l):
    color = [-1] * l
    for v in g:
        if color[v] == -1:
            if not is_bipartite_helper(g,color,v):
                return False
    return True


def is_bipartite_helper(g,color,v):
    q = []
    q.append(v)
    color[v] = 1
    while q:
        u = q.pop(0)
        for e in g[u]:
            if color[e] == -1:
                color[e] = 1-color[u]
            else:
                if color[e] == color[u]:
                    return False
            q.append(e)
    return True

if __name__ == '__main__':
    g = {1: [4,5], 2: [5,6], 3: [6], 4: [1,2], 5: [2,1], 6:[3]}
    g1 = {1: [2,3], 2: [4,3], 3: [1,4]}
    print is_bipartite(g1,5)



