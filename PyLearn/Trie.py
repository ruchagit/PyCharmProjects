class TrieNode:
    def __init__(self, parent, value):
        self.parent = parent
        self.children = dict()
        self.value = value
        self.isWord = False
        if parent:
            parent.children[value] = self


def MakeTrie(dictionary):
    root = TrieNode(None,-1)
    for word in dictionary:
        currNode = root
        for c in word:
            if c not in currNode.children:
                TrieNode(currNode,c)
            currNode = currNode.children[c]
        currNode.isWord = True
    return root

def findWords(dictionaryList, board):
    root = MakeTrie(dictionaryList)
    rows = len(board)
    cols = len(board[0])
    queue = []
    words = []

    for i in range(rows):
        for j in range(cols):
            if board[i][j] in root.children:
                queue.append((i,j,board[i][j],root.children[board[i][j]]))
                if root.children[board[i][j]].isWord:
                    words.append(board[i][j])

    while queue:
        i, j, s, node = queue[0]
        del queue[0]
        for a in range(max(0, i - 1), min(rows, i + 2)):
            for b in range(max(0, j - 1), min(cols, j + 2)):
                if (a,b) != (i,j) and board[a][b] in node.children:
                    s2 = s + board[a][b]
                    node2 = node.children[board[a][b]]
                    queue.append((a,b,s2,node2))
                    if node2.isWord:
                        words.append(s2)
    return words

if __name__ == '__main__':
    words = findWords(["GEEKS", "FOR", "QUIZ", "GEEK","*","GEEKED","*&"],
                  [['G','I','Z','O','*','A'],
                  ['U','E','K','A','&','B'],
                  ['Q','S','E','E','D','C'],
                  ['A','B','C','H','H','O'],
                  ['K','J','H','G','F','Z']])
    print words
    