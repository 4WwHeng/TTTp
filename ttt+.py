player = ['Lx', 'Sx']
opponent = ['Lo', 'So']

def evaluate(board):
    for row in range(0, 3):
        if all(board[row][i] in player for i in range(3)):
            return -10
        elif all(board[row][i] in opponent for i in range(3)):
            return 10
    for col in range(0, 3):
        if all(board[i][col] in player for i in range(3)):
            return -10
        elif all(board[i][col] in opponent for i in range(3)):
            return 10
    if all(board[i][i] in player for i in range(3)):
        return -10
    if all(board[i][i] in opponent for i in range(3)):
        return 10
    if all(board[i][2-i] in player for i in range(3)):
        return -10
    if all(board[i][2-i] in opponent for i in range(3)):
        return 10
    return 0

def MovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False

mem = {}
for i in range(3):
    for j in range(3):
        mem[(i,j)] = False

mem2 = {}
def minimax(board, depth, isMax, RLx, RSx, RLo, RSo,A,B):
    score = evaluate(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if depth == 5:
        return 0

    if MovesLeft(board) == True:
        if isMax:
            best = -10
            if RLo:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == '_':
                            board[i][j] = 'Lo'
                            best = max(best,minimax(board,depth+1,not isMax,RLx,RSx,RLo-1,RSo,A,B))
                            board[i][j] = '_'
                            A = max(A, best)
                            if B <= A:
                                break

                        if board[i][j] == 'Sx':
                            board[i][j] = 'Lo'
                            best = max(best,minimax(board,depth+1,not isMax,RLx,RSx,RLo-1,RSo,A,B))
                            board[i][j] = 'Sx'
                            A = max(A, best)
                            if B <= A:
                                break

            if RSo:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == '_':
                            board[i][j] = 'So'
                            mem[(i,j)] = True
                            best = max(best,minimax(board,depth+1,not isMax,RLx,RSx,RLo,RSo-1,A,B))
                            board[i][j] = '_'
                            A = max(A, best)
                            if B <= A:
                                break
                            mem[(i,j)] = False
            return best
        else:
            best = 10
            if RLx:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == '_':
                            board[i][j] = 'Lx'
                            best = min(best,minimax(board,depth+1,not isMax,RLx-1,RSx,RLo,RSo,A,B))
                            board[i][j] = '_'
                            B = min(B, best)
                            if B <= A:
                                break
                        if board[i][j] == 'So':
                            board[i][j] = 'Lx'
                            best = min(best,minimax(board,depth+1,not isMax,RLx-1,RSx,RLo,RSo,A,B))
                            board[i][j] = 'So'
                            B = min(B, best)
                            if B <= A:
                                break

            if RSx:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == '_':
                            board[i][j] = 'Sx'
                            mem[(i,j)] = True
                            best = min(best,minimax(board,depth+1,not isMax,RLx,RSx-1,RLo,RSo,A,B))
                            board[i][j] = '_'
                            B = min(B, best)
                            if B <= A:
                                break
                            mem[(i,j)] = True
            return best
    return 0
def findBestMove(board, RLo, RSo, RLx, RSx):
    bestVal = -1000
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if RLo:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == '_':
                            board[i][j] = 'Lo'
                            moveVal = minimax(board, 0, False, RLx, RSx, RLo - 1, RSo,-1000,1000)
                            board[i][j] = '_'
                            if moveVal > bestVal:
                                bestMove = (i, j, 'Lo')
                                bestVal = moveVal
                        if board[i][j] == 'Sx':
                            board[i][j] = 'Lo'
                            moveVal = minimax(board, 0, False, RLx, RSx, RLo - 1, RSo,-1000,1000)
                            board[i][j] = 'Sx'
                            if moveVal > bestVal:
                                bestMove = (i, j, 'Lo')
                                bestVal = moveVal
            if RSo:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == '_':
                            board[i][j] = 'So'
                            mem[(i, j)] = True
                            moveVal = minimax(board, 0, False, RLx, RSx, RLo, RSo - 1,-1000,1000)
                            board[i][j] = '_'
                            mem[(i, j)] = False
                            if moveVal > bestVal:
                                bestMove = (i, j, 'So')
                                bestVal = moveVal
    return bestMove

def printBoard(board):
    print(board[0])
    print(board[1])
    print(board[2])

board = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
from random import randint
goFirst = randint(0,1)
R = {}
R['Lo'] = 3
R['So'] = 3
R['Lx'] = 3
R['Sx'] = 3

while MovesLeft(board) and evaluate(board) == 0:
    if goFirst == 1:
        comp = findBestMove(board,3,3,3,3)
        board[comp[0]][comp[1]] = comp[2]
        R[comp[2]] -= 1
        print('\n')
        print('opponent goes')
        printBoard(board)
        goFirst = 0
    ipt1 = input('Big(0) or Small(1)').strip()
    ipt2 = input('Write Coor of ur move: (eg: 0 0)').split()
    if ipt1 == '0':
        board[int(ipt2[0])][int(ipt2[1])] = 'Lx'
        R['Lx'] -= 1
    else:
        board[int(ipt2[0])][int(ipt2[1])] = 'Sx'
        R['Sx'] -= 1
    printBoard(board)
    if not MovesLeft(board) or evaluate(board) != 0:
        break
    comp = findBestMove(board,R['Lo'],R['So'],R['Lx'],R['Sx'])
    board[comp[0]][comp[1]] = comp[2]
    R[comp[2]] -= 1
    print('\n')
    print('opponent goes')
    printBoard(board)
