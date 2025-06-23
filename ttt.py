def evaluate(board):
    for row in range(0, 3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == 'x':
                return -1
            elif board[row][0] == 'o':
                return 1
    for col in range(0, 3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == 'x':
                return -1
            elif board[0][col] == 'o':
                return 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'x':
            return -1
        elif board[0][0] == 'o':
            return 1
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == 'x':
            return -1
        elif board[0][2] == 'o':
            return 1
    return 0
def MovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False
def minimax(board, isMax):
    score = evaluate(board)
    if score == 1:
        return score
    if score == -1:
        return score
    if MovesLeft(board) == False:
        return 0

    if isMax:
        best = -1
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    best = max(best, minimax(board, not isMax))
                    board[i][j] = '_'
        return best
    else:
        best = 1
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    best = min(best, minimax(board, not isMax))
                    board[i][j] = '_'
        return best

def findBestMove(board):
    bestVal = -1
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = opponent
                moveVal = minimax(board, False)
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove

def printBoard(board):
    print(board[0])
    print(board[1])
    print(board[2])
player = 'x'
opponent = 'o'
board = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
from random import randint
goFirst = randint(0,1)
while MovesLeft(board) and evaluate(board) == 0:
    print(''.join([''.join(i) for i in board]))
    if goFirst == 1:
        comp = findBestMove(board)
        board[comp[0]][comp[1]] = opponent
        print('\n')
        print('opponent goes')
        printBoard(board)
        goFirst = 0
    ipt = input('Write Coor of ur move:').split()
    board[int(ipt[0])][int(ipt[1])] = player
    printBoard(board)
    if not MovesLeft(board) or evaluate(board) != 0:
        break
    comp = findBestMove(board)
    board[comp[0]][comp[1]] = opponent
    print('\n')
    print('opponent goes')
    printBoard(board)


