def safe(g, u, c, V):
    for i in range(V):
        if g[u][i] == 1 and color[i] == c:
            return False
    return True

def graphutil(g, m, V, color, u):
    if u == V:
        return True
    for i in range(1,m+1):
        if safe(g,u,i,V):
            color[u] = i
            if graphutil(g,m,V,color,u+1):
                return True
            color[u] = 0
    return False


if __name__ == '__main__':
    g = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]
    m = 3
    V = 4
    color = [0] * V
    print graphutil(g,m,V,color,0)
    print color