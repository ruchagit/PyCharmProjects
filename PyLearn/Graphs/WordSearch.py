from copy import copy

def word_search1(mat,word):
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            # q = []
            if word[0] == mat[r][c]:
                # q.append((r,c))
                # if start_search_bfs(mat,word,q):
                #     return True
                if start_search(mat,r,c,word,1):
                    return True
    return False

def start_search(mat,r,c,word,w):
    if w == len(word):
        return True
    pw = mat[r][c]
    mat[r][c] = None
    minr = max(0, r - 1)
    minc = max(0, c - 1)
    maxr = min(len(mat)-1, r + 1)
    maxc = min(len(mat[0])-1, c + 1)
    if mat[minr][c] != None and mat[minr][c] == word[w]:
        if start_search(mat,minr,c,word,w+1):
            return True
    if mat[maxr][c] != None and mat[maxr][c] == word[w]:
        if start_search(mat,maxr,c,word,w+1):
            return True
    if mat[r][minc] != None and mat[r][minc] == word[w]:
        if start_search(mat,r,minc,word,w+1):
            return True
    if mat[r][maxc] != None and mat[r][maxc] == word[w]:
        if start_search(mat,r,maxc,word,w+1):
            return True
    mat[r][c] = pw
    return False

def start_search_bfs(mat,word,q):
    i = 1
    while q:
        update = False
        r,c = q[0]
        print r,c
        del q[0]
        minr = max(0, r - 1)
        minc = max(0, c - 1)
        maxr = min(len(mat) - 1, r + 1)
        maxc = min(len(mat[0]) - 1, c + 1)
        if mat[minr][c] == word[i] and minr != r:
            q.append((minr,c))
            print "1"
            update = True
        if mat[maxr][c] == word[i] and maxr != r:
            q.append((maxr,c))
            print "2"
            update = True
        if mat[r][minc] == word[i] and minc != c:
            q.append((r,minc))
            print "3"
            update = True
        if mat[r][maxc] == word[i] and maxc != c:
            q.append((r,maxc))
            print "4"
            update = True
        if update:
            i += 1
        else:
            return False
        if i == len(word):
                return True
    return False





if __name__ == '__main__':
    mat = [
              ['A','B','C','E'],
              ['S','F','C','S'],
              ['A','D','E','E']
          ]
    mat1 = [['C','A','A'],
            ['A','A','A'],
            ['B','C','D']]
    w1 = "AAB"
    print word_search1(mat1,"AAB")


