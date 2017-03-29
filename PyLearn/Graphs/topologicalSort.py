def topological_sort(g,V):
    visited = [False] * V
    stack = []
    for u in g:
        if not visited[u]:
            dfs_helper(g,u,visited,stack)
    stack.reverse()
    return stack


def dfs_helper(g,v,visited,stack):
    visited[v] = True
    for e in g[v]:
        if not visited[e]:
            dfs_helper(g,e,visited,stack)
    stack.append(v)

if __name__ == '__main__':
    g = {1: [], 2: [3], 3: [1], 4: [1,0], 5: [2,0], 0: []}
    print topological_sort(g,6)