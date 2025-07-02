from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().strip())))

# print(graph)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if (0<=nx<=n-1) and (0<=ny<=m-1):
        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          queue.append((nx, ny))
  return graph[n-1][m-1]
  
result = bfs(0,0)
print(result)