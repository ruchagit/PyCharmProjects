def reverse_graph(g):
    revg = dict()
    for v in g:
        for e in g[v]:
            if e in revg:
                revg[e].append(v)
            else:
                revg[e] = [v]
    return revg

def scc(g,v):
    visited = [False] * v
    res = [[]]
    revg = reverse_graph(g)
    stack = dfs(revg,v)
    while stack:
        u = stack.pop()
        if not visited[u]:
            s = []
            dfs_helper(g,u,visited,s)
            res.append(s)
    return res

def dfs(g,v):
    visited = [False] * v
    stack = []
    for e in g:
        if not visited[e]:
            dfs_helper(g,e,visited,stack)
    return stack

def dfs_helper(g,v,visited,stack):
    visited[v] = True
    for e in g[v]:
        if not visited[e]:
            dfs_helper(g,e,visited,stack)
    stack.append(v)
    # print stack, "-->"

if __name__ == '__main__':
    g = dict()
    g = {1: [2], 2: [1, 3], 3: [1,5], 4: [5], 5: [4]}
    print scc(g,6)
    # revg = reverse_graph(g)
    # print revg