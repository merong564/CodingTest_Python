from sys import stdin
from collections import deque

def solution(arr):

    cases = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    visited = [False] * 512
    visited[int(''.join(arr), 2)] = True
	# BFS
    queue = deque([(int(''.join(arr), 2), 0)])
    while queue:
        arrBin, count = queue.popleft()

        if arrBin == 0 or arrBin == 511:
            return count

        for numbers in cases:
            newArr = flip(numbers, list(bin(arrBin)[2:].zfill(9)))
            vs = int(''.join(newArr), 2)
            if not visited[vs]:
                visited[vs] = True
                queue.append((int(''.join(newArr), 2), count+1))
    
    return -1

def flip(numbers, arr):
    for num in numbers:
        arr[num] = '0' if arr[num] == '1' else '1'
    return arr

T = int(stdin.readline())

for _ in range(T):
    arr = list(list(stdin.readline().split()) for _ in range(3))
    arr = ['1' if arr[y][x]=='H' else '0' for y in range(3) for x in range(3)]
    print(solution(arr))


## BFS 답안
from collections import deque

def make_bin(arr: list):
  a = []
  for i in arr:
    for j in i:
      a.append(i)
  n = int(''.joint(map(str, a)), 2)
  return n

t = int(input())
for _ in range(t):
  input_arr = [list(map(str, input().split())) for _ in range(3)]
  arr = []
  for k in range(3):
    new_arr = list(map(lambda v: 1 if v == 'H' else 0, input_arr[k]))
    arr.append(new_arr)

cases = [[0, 3, 6], 
        [1, 4, 7], 
        [2, 5, 8], 
        [0, 1, 2], 
        [3, 4, 5], 
        [6, 7, 8], 
        [2, 4, 6],
        [0, 4, 8]]

visited = [False]*512
q = deque()
bin_n = make_bin(arr)
q.append((bin_n, 0))
visited[bin_n] = True
answer = -1

while q:
  num, cnt = q.popleft()
  if num == 0 or num == 511:
    answer = cnt
    break

  for case in cases:
    b_num = list(bin(num)[2:].zfill(9))

    for c in case:
      b_num[c] = '0' if b_num[c] == '1' else '1'
    chngd_num = int(''.join(b_num), 2)

    if not visited[chngd_num]:
      visited[chngd_num] = True
      q.append((chgnd_num, cnt+1))

print(answer)
  

## 내 답안: DFS로 풀었는데 출력 안나옴
# import sys
# sys.setrecursionlimit(10**8)
# input = sys.stdin.readline

# def find(matrix, cnt, before):
#   global min_cnt

#   if cnt >= min_cnt:
#     return 
    
#   if matrix == want[0] or matrix == want[1]:
#     min_cnt = cnt
#     return
    
#   for i in range(8):
#     if before == i:
#       continue
#     new_matrix = cal(i, matrix)
#     find(new_matrix, cnt+1, i)

  
# def cal(num, matrix):
#   new_matrix = [row[:] for row in matrix]
  
#   if num == 0:
#     for i in range(3):
#       new_matrix[i][0] *= -1

#   if num == 1:
#     for i in range(3):
#       new_matrix[i][1] *= -1

#   if num == 2:
#     for i in range(3):
#       new_matrix[i][2] *= -1

#   if num == 3:
#     for i in range(3):
#       new_matrix[0][i] *= -1

#   if num == 4:
#     for i in range(3):
#       new_matrix[1][i] *= -1

#   if num == 5:
#     for i in range(3):
#       new_matrix[2][i] *= -1

#   if num == 6:
#     for i in range(3):
#       new_matrix[i][i] *= -1

#   if num == 7:
#     for i in range(3):
#       new_matrix[i][2-i] *= -1

#   return new_matrix


# t = int(input())
# matrix_list = []
# for _ in range(t):
#   matrix = [[] for _ in range(3)]
#   for i in range(3):
#     row = list(map(str, input().split()))
#     print(row)
#     for c in row:
#       if c == 'H':
#         matrix[i].append(1)
#       else:
#         matrix[i].append(-1)
#   matrix_list.append(matrix)

# want = [[[1]*3 for _ in range(3)], [[-1]*3 for _ in range(3)]]
# cnt_list = []

# for i in range(t):
#   cnt = 0
#   before = 100
#   min_cnt = float('inf')
#   print(f'{i}번째 matrix: {matrix_list[i]}')
#   find(matrix_list[i], cnt, before)
#   cnt_list.append(min_cnt)
#   print(min_cnt)

# for i in range(t):
#   print(cnt_list[i])
