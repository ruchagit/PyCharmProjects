def matrix_game(mat,r,c,moves):
    if game_solved(mat):
        return True
    for i in range(1,5):
        if move_possible(r,c,moves[i]):
            new_r = r+moves[i][0]
            new_c = c+moves[i][1]
            temp = mat[r][c]
            mat[r][c] = mat[new_r][new_c]
            mat[new_r][new_c] = temp
            return matrix_game(mat,new_r,new_c,moves)

def move_possible(r,c,move):
    if 0 <= r+move[0] <= 2:
        if 0 <= c+move[1] <= 2:
            return True
    return False

def game_solved(mat):
    i = 1
    for r in range(3):
        for c in range(3):
            if r == 2 and c == 2:
                return mat[2][2] == 0
            if mat[r][c] != i:
                return False
            i += 1
    return True


def func():
    l = [1,2,3,4]
    for i in range(len(l)):
        print i
        l.append(0)

if __name__ == '__main__':
    # moves = dict()
    # moves[1] = (0,-1)
    # moves[2] = (0,1)
    # moves[3] = (-1,0)
    # moves[4] = (1,0)
    # mat = [[1,2,3],
    #        [4,5,6],
    #        [7,0,8]]
    # print matrix_game(mat,2,1,moves)
    func()
