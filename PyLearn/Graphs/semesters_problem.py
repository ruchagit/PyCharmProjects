def indeg_array(g):
    indeg = dict()
    for v in g:
        if v not in indeg:
            indeg[v] = 0
        for e in g[v]:
            if e in indeg:
                indeg[e] += 1
            else:
                indeg[e] = 1
    return sems_req(g,indeg,0)

def sems_req(g,indeg,count):
    q = []
    if len(indeg) == 0:
        return count
    for i in indeg.keys():
        if indeg[i] == 0:
            q.append(i)
            del indeg[i]
    count += 1
    return process_q(q,g,count,indeg)

def process_q(q,g,count,indeg):
    while q:
        u = q.pop(0)
        for e in g[u]:
            if e in indeg:
                indeg[e] -= 1
    return sems_req(g,indeg,count)


if __name__ == '__main__':
    g = {1: [3], 2: [3], 3: [4,5], 4: [], 5: [], 6: [7], 7:[]}
    print indeg_array(g)
