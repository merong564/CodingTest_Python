import sys
from collections import deque
input = sys.stdin.readline

dx = [2, 2, 1, 1, -2, -2, -1, -1]
dy = [1, -1, 2, -2, 1, -1, 2, -2]

def bfs(x_start, y_start, x_d, y_d):
    queue = deque()
    queue.append((x_start,y_start))
    while queue:
        x, y = queue.popleft()
        #visited[x][y] = True       # 여기에 두면 안됨. 방문했을 때만 True처리 필요
        if (x == x_d) and (y == y_d):
            return matrix[x][y]
        for i in range(0, 8):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0<=nx<l) and (0<=ny<l) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                matrix[nx][ny] = matrix[x][y] + 1

list = []

t = int(input())
for _ in range(t):
    l = int(input())
    matrix = [[0]*l for _ in range(l)]
    visited = [[False]*l for _ in range(l)]
    x_s, y_s = map(int, input().split())
    x_d, y_d = map(int, input().split())
    result = bfs(x_s, y_s, x_d, y_d)
    list.append(result)

for i in range(t):
    print(list[i])