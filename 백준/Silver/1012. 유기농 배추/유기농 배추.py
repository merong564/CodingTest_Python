## DFS 내 풀이
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**5)

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def dfs(x, y, graph):
#   if graph[x][y]:
#     graph[x][y] = 0
#     for i in range(4):
#       nx = x+dx[i]
#       ny = y+dy[i]

#       if nx<0 or nx>=n or ny<0 or ny>=m:
#         continue

#       dfs(nx, ny, graph)

#     return True

# t = int(input())
# result = [0]*t


# for q in range(t):
#   cnt = 0
#   # input 처리
#   m, n, k = map(int, input().split())
#   graph = [[0]*m for _ in range(n)]
#   for _ in range(k):
#     a, b = map(int, input().split())
#     graph[b][a] = 1

#   # dfs 수행
#   for i in range(n):
#     for j in range(m):
#       section = dfs(i, j, graph)
#       if section:
#         cnt += 1
        
#   result[q] = cnt

# for i in range(t):
#   print(result[i])

## DFS 다른 답안 (더 깔끔)
# import sys
# sys.setrecursionlimit(10**5)

# def dfs(x, y):
#   dx = [1, -1, 0, 0]
#   dy = [0, 0, 1, -1]

#   for i in range(4):
#     nx = x+dx[i]
#     ny = y+dy[i]

#     # 범위 안에 있으면서
#     if (0<=nx<n) and (0<=ny<m):
#       if matrix[nx][ny] == 1:  # 값이 1일 때만 탐색 진행
#         matrix[nx][ny] = -1
#         dfs(nx, ny)
        
# t = int(input())
# for _ in range(t):
#   m, n, k = map(int, input().split())
#   matrix = [[0]*m for _ in range(n)]
#   cnt = 0

#   for _ in range(k):
#     b, a = map(int, input().split())
#     matrix[a][b] = 1

#   for i in range(n):
#     for j in range(m):
#       if matrix[i][j] > 0:
#         dfs(i, j)
#         cnt += 1
  
#   print(cnt)

## BFS 풀이
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

def bfs(x, y):  
  queue.append((x,y))
  matrix[x][y] = 0

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if (0<=nx<n) and (0<=ny<m):
        if matrix[nx][ny] == 1:
          queue.append((nx, ny))
          matrix[nx][ny] = 0

for _ in range(t):
  m, n, k = map(int, input().split())
  matrix = [[0]*m for _ in range(n)]
  cnt = 0
  for _ in range(k):
    b, a = map(int, input().split())
    matrix[a][b] = 1

  for i in range(n):
    for j in range(m):
      if matrix[i][j] == 1:
        bfs(i, j)
        cnt += 1
  print(cnt)
  
