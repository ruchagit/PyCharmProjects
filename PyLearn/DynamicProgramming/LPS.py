def LPS(seq):
    n = len(seq)
    mat = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        mat[i][i] = 1
    for curr_len in range(2,n+1):
        for i in range(0,n-curr_len+1):
            j = i+curr_len-1
            if seq[i] == seq[j]:
                mat[i][j] = mat[i+1][j-1] + 2
            else:
                mat[i][j] = max(mat[i+1][j], mat[i][j-1])
    return mat[0][n-1]


def test(arr,i, k,  path, loc):

    if i == len(arr):
        if k == 0:
            return
        test(arr,0, k-1, path, loc)
        return

    if arr[i] == 'g':
        if loc[2] == 0:
            loc[1] += 1
        elif loc[2] == 1:
            loc[0] += 1
        elif loc[2] == 2:
            loc[1] -= 1
        else:
            loc[0] -= 1
        path[loc[0]][loc[1]] =  1
    elif arr[i] == 'l':
        loc[2] = (loc[2] + 3)%4
    else:
        loc[2] = (loc[2] + 1)%4
    test(arr,i+1,k, path,loc)


def doesCircleExist(commands):
    n = len(commands)
    res = ["NO"] * n
    for i in range(n):
        d = ''

        for j in range(len(commands[i])):
            if commands[i][j] == 'L':
                if d == '':
                    d = 'L'
                elif d == 'R':
                    d = ''
            elif commands[i][j] == 'R':
                if d == '':
                    d = 'R'
                elif d == 'L':
                    d = ''
        if d != '':
            res[i] = "YES"
    return res


def spiralMatrix():
    n1, n2 = raw_input().split(',')
    n1 = int(n1)
    n2 = int(n2)
    mat = [[int(x) for x in raw_input().split(',')] for x in range(n1)]
    row_start = 0
    row_end = len(mat)-1
    col_start = 0
    col_end = len(mat[0])-1
    res = []
    while row_start <= row_end and col_start <= col_end:
        for col in range(col_start, col_end+1):
            res.append(mat[row_start][col])
        row_start += 1
        for row in range(row_start, row_end+1):
            res.append(mat[row][col_end])
        col_end -=1
        for col in range(col_end, col_start-1, -1):
            res.append(mat[row_end][col])
        row_end -= 1
        for row in range(row_end, row_start-1, -1):
            res.append(mat[row][col_start])
        col_start += 1
    print res



if __name__ == '__main__':
    # seq = ['a','c','g','t','g','t','c','a','a','a','a','t','c','g']
    # seq = ['a', 'c', 'g', 'a','a','a']
    # print LPS(seq)
    # M = 51
    # ar = [[0 for x in range(M)] for x in range(M)]
    # ar[M//2][M//2] = 1
    # test("grglgrlrl",0, 10, ar, [M//2,M//2,0])
    # for r in range(M):
    #     print r, ''.join(['x' if x == 1 else ' ' for x in ar[r]])
    spiralMatrix()