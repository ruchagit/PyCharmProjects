import topologicalSort

def shortest_path(g,V,src,cost):
    order = topologicalSort.topological_sort(g,V)
    dist = [float('inf')] * V
    par = [float('inf')] * V
    dist[src] = 0
    par[src] = -1
    for u in order:
        for v in g[u]:
            relax(u,v,dist,cost,par)
    print "parent array : ", par
    return dist

def relax(u,v,dist,cost,par):
    if dist[v] > dist[u] + cost[(u,v)]:
        dist[v] = dist[u] + cost[(u, v)]
        par[v] = u

if __name__ == '__main__':
    g = {1: [2,4,3], 2: [3,4], 3: [0], 4: [0], 5: [1,2], 0: []}
    cost = {(5,1): 1, (5,2): 3, (1,2): 6, (1,4): 6, (2,3): 1,
            (2,4): 2, (3,0): 3, (4,0): 1, (1,3): 5}
    print shortest_path(g,6,1,cost)

