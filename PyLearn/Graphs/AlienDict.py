class Graph:
    def __init__(self):
        self.V = 0
        self.vertices = set()
        self.adj = dict()
        self.visited = dict()
        self.cycle = dict()

    def add_vertex(self, v):
        if v not in self.vertices:
            self.adj[v] = set()
            self.vertices.add(v)
            self.V += 1
            self.visited[v] = False
            self.cycle[v] = "W"

    def add_edge(self, f, t):
        if f not in self.adj:
            self.adj[f] = set()
            self.adj[f].add(t)
        else:
            self.adj[f].add(t)

    def topological_sort_helper(self, f, stack):
        self.visited[f] = True
        for node in self.adj[f]:
            if not self.visited[node]:
                self.topological_sort_helper(node, stack)
        stack.append(f)

    def topological_sort(self):
        stack = []
        for i in self.vertices:
            if not self.visited[i]:
                self.topological_sort_helper(i, stack)
        return stack

    def detect_cycle_helper(self,node):
        self.cycle[node] = "G"
        # if node in self.adj:
        for n in self.adj[node]:
            if self.cycle[n] == "W" and self.detect_cycle_helper(n):
                return True
            elif self.cycle[n] == "G":
                return True
        self.cycle[node] = "B"
        return False

    def detect_cycle(self):
        for i in self.vertices:
            if self.cycle[i] == "W":
                if self.detect_cycle_helper(i):
                    return True
        return False


def word_to_vertices(g,word):
    for w in word:
        g.add_vertex(w)

def alien_dict(g,words):
    if len(words) == 1:
        return words[0][::-1]
    for i in range(len(words)-1):
        w1 = words[i]
        word_to_vertices(g,w1)
        w2 = words[i+1]
        word_to_vertices(g,w2)
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                g.add_edge(w1[j], w2[j])
                break
    if g.detect_cycle():
        return ""
    stack = g.topological_sort()
    res = ""
    while stack:
        res += stack.pop()
    return res


if __name__ == '__main__':
    a = ord('a')
    g = Graph()
    words1 = ["baa","abcd","abca","cab","cad"]
    words2 = ["abcf", "abda", "eb", "ebc", "ecc", "bdcc"]
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    words3 = ["x","z","x"]
    # words = ["abc", "abd", "eb", "ebc", "ecc"]
    print alien_dict(g,words)

