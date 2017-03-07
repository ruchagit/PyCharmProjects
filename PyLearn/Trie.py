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

def findWords_dfs(dictionaryList, board):
    root = MakeTrie(dictionaryList)
    rows = len(board)
    cols = len(board[0])
    res = []
    for i in range(rows):
        for j in range(cols):
            if board[i][j] in root.children:
                next_node = root.children[board[i][j]]
                if next_node.isWord:
                    res.append(board[i][j])
                else:
                    dfs_helper(i,j,board,next_node,res,board[i][j])
                if len(res) == len(dictionaryList):
                    return res
    return res

def dfs_helper(r,c,board,node,res,s):
    ans = False
    if node.isWord and s not in res:
        res.append(s)
        return True
    pw = board[r][c]
    board[r][c] = None
    minr = max(0, r - 1)
    minc = max(0, c - 1)
    maxr = min(len(board) - 1, r + 1)
    maxc = min(len(board[0]) - 1, c + 1)
    if dfs_helper_helper(minr,c,board,node,res,s):
        # board[r][c] = pw
        ans = True
        # return True
    if dfs_helper_helper(maxr,c,board,node,res,s):
        # board[r][c] = pw
        ans = True
        # return True
    if dfs_helper_helper(r,minc,board,node,res,s):
        # board[r][c] = pw
        ans = True
        # return True
    if dfs_helper_helper(r,maxc,board,node,res,s):
        # board[r][c] = pw
        ans = True
        # return True
    board[r][c] = pw
    return ans
    # if board[minr][c] and board[minr][c] in node.children:
    #     next_node = node.children[board[minr][c]]
    #     next_s = s + board[minr][c]
    #     if dfs_helper(minr,c,board,next_node,res,next_s):
    #         board[r][c] = pw
    #         return True
    # if board[maxr][c] and board[maxr][c] in node.children:
    #     next_node = node.children[board[maxr][c]]
    #     next_s = s + board[maxr][c]
    #     if dfs_helper(maxr,c,board,next_node,res,next_s):
    #         board[r][c] = pw
    #         return True
    # if board[r][minc] and board[r][minc] in node.children:
    #     next_node = node.children[board[r][minc]]
    #     next_s = s + board[r][minc]
    #     if dfs_helper(r,minc,board,next_node,res,next_s):
    #         board[r][c] = pw
    #         return True
    # if board[r][maxc] and board[r][maxc] in node.children:
    #     next_node = node.children[board[r][maxc]]
    #     next_s = s + board[r][maxc]
    #     if dfs_helper(r,maxc,board,next_node,res,next_s):
    #         board[r][c] = pw
    #         return True
    # board[r][c] = pw
    # return False

def dfs_helper_helper(r,c,board,node,res,s):
    if board[r][c] and board[r][c] in node.children:
        next_node = node.children[board[r][c]]
        next_s = s + board[r][c]
        if dfs_helper(r,c,board,next_node,res,next_s):
            return True
    return False

def to2d(arr):
    mat = [list(x) for x in arr]
    return mat

if __name__ == '__main__':
    mat =   [['C','A','A'],
            ['A','A','A'],
            ['B','C','D']]
    w = ["AAB"]
    mat1 = [
              ['o','a','a','n'],
              ['e','t','a','e'],
              ['i','h','k','r'],
              ['i','f','l','v']
           ]
    w1 = ["oath","pea","eat","rain"]

    mat2 = [['a','b'],
            ['c','d']]
    w2 = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]

    mat3 = [['a','b'],
            ['a','a']]
    w3 = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]

    mat4 = to2d(["seenew","tmriva","obsibd","wmysen","ltsnsa","iezlgn"])
    # words = findWords(["GEEKS", "FOR", "QUIZ", "GEEK","*","GEEKED","*&"],
    #               [['G','I','Z','O','*','A'],
    #               ['U','E','K','A','&','B'],
    #               ['Q','S','E','E','D','C'],
    #               ['A','B','C','H','H','O'],
    #               ['K','J','H','G','F','Z']])
    words = findWords_dfs(["besan"],mat4)
    print words


# def findWords(dictionaryList, board):
#     root = MakeTrie(dictionaryList)
#     rows = len(board)
#     cols = len(board[0])
#     queue = []
#     words = []
#
#     for i in range(rows):
#         for j in range(cols):
#             if board[i][j] in root.children:
#                 queue.append((i,j,board[i][j],root.children[board[i][j]]))
#                 if root.children[board[i][j]].isWord:
#                     words.append(board[i][j])
#
#     while queue:
#         i, j, s, node = queue.pop(0)
#         for a in range(max(0, i - 1), min(rows, i + 2)):
#             for b in range(max(0, j - 1), min(cols, j + 2)):
#                 if (a,b) != (i,j) and board[a][b] in node.children:
#                     s2 = s + board[a][b]
#                     node2 = node.children[board[a][b]]
#                     queue.append((a,b,s2,node2))
#                     if node2.isWord:
#                         words.append(s2)
#     return words