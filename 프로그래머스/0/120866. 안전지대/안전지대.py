def solution(board):
    answer = 0
    m = len(board)
    n = len(board[0])
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                board = bomb(board, i, j)
    # print(board)
    for row in board:
        answer += row.count(0)
    return answer
                
def bomb(board, i, j):
    m = len(board)
    n = len(board[0])
    
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            if (0<=i+a<m and 0<=j+b<n) and board[i+a][j+b] == 0:
                board[i+a][j+b] = 2
                
    return board
            