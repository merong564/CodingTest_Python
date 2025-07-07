from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
matrix = []
queue = deque()

for i in range(n):
    row = list(map(int, input().split()))
    for j, val in enumerate(row):
        if val == 1:
            queue.append((i, j, 0))  # (x, y, day)
    matrix.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_day = 0

while queue:
    x, y, day = queue.popleft()
    max_day = max(max_day, day)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = 1  # 방문 처리
                queue.append((nx, ny, day + 1))

# 확인
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            print(-1)
            sys.exit()
print(max_day)
