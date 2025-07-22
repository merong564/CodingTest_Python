## 내 답안
# import sys
# sys.setrecursionlimit(10**5)


# def find(board):
#   global result
#   if board == '':
#     return
    
#   if board[:4] == 'XXXX':
#     result += 'AAAA'
#     new_board = board[4:]
#     find(new_board)

#   elif board[:2] == 'XX':
#     result += 'BB'
#     new_board = board[2:]
#     find(new_board)

#   elif board[0] == '.':
#     result += '.'
#     new_board = board[1:]
#     find(new_board)

#   else:
#     print(-1)
#     sys.exit()

# board = str(input())
# cnt = 0
# result = ''
# find(board)
# print(result)

## 다른 사람 답안 (겁나 간단함)
board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
  print(-1)

else:
  print(board)
