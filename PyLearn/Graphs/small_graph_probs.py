def two_degree(g):
    t_deg = dict()
    for v in g:
        t_deg[v] = 0
        for e in g[v]:
            t_deg[v] += len(g[e])
    return t_deg

def detect_cycle(g, scc, cycle):
    visited = dict()
    count = 0
    for v in g:
        if v not in visited:
            scc[count] = []
            visited[v] = False
            is_cycle = detect_cycle_helper(g,v,visited,-1,count,scc)
            cycle[count] = is_cycle
        count += 1

def detect_cycle_helper(g, v, visited, parent,c,scc):
    visited[v] = True
    scc[c].append(v)
    is_cycle = False
    for u in g[v]:
        is_cycle &= False
        if u == parent:
            continue
        elif u not in visited:
            visited[u] = False
            detect_cycle_helper(g, u, visited, v,c,scc)
        elif u in visited and visited[u]:
            is_cycle = True
    return is_cycle


def dfs(g,src,n):
    visited = [False] * (n+1)
    possible = [False] * (n+1)
    possible[src] = True
    possible[0] = True
    for v in g:
        if v == src: continue
        for e in g[v]:
            if possible[e]:
                possible[v] = True
            elif not visited[e]:
                if dfs_helper(g,e,src,possible,visited):
                    possible[v] = True
    # print possible
    for i in range(1,len(possible)):
        if not possible[i]:
            return False
    return True

def dfs_helper(g,v,src,possible,visited):
    visited[v] = True
    for e in g[v]:
        if e == src:
            possible[v] = True
            return True
        if possible[e]:
            possible[v] = True
            return True
        if not visited[e]:
            if dfs_helper(g,e,src,possible,visited):
                possible[v] = True
                return True
    return False

if __name__ == '__main__':
    g = {1: [4,5], 2: [5,6], 3: [6], 4: [1,2], 5: [2,1], 6:[3]}
    g1 = {1: [5,2,3], 2: [1,3], 3: [4,2,1], 4:[3], 5:[1], 6:[7], 7:[6]}
    g2 = {1:[2,4,5], 2:[3], 3:[1], 4:[6,7], 5:[8],
          6:[8], 7:[8], 8:[1]}
    # t = two_degree(g1)
    # print t
    #-----
    # scc = dict()
    # cycle = dict()
    # detect_cycle(g1,scc,cycle)
    # print scc
    # print cycle
    #---
    print dfs(g2,1,8)