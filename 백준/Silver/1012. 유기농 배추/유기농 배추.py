import sys
# from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, graph):
  if graph[x][y]:
    graph[x][y] = 0
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue

      dfs(nx, ny, graph)

    return True

t = int(input())
result = [0]*t


for q in range(t):
  cnt = 0
  # input 처리
  m, n, k = map(int, input().split())
  graph = [[0]*m for _ in range(n)]
  for _ in range(k):
    a, b = map(int, input().split())
    graph[b][a] = 1

  # dfs 수행
  for i in range(n):
    for j in range(m):
      section = dfs(i, j, graph)
      if section:
        cnt += 1
        
  result[q] = cnt

for i in range(t):
  print(result[i])