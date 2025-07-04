import sys
# from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m, k = map(int, input().split())
matrix = [[0]*m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, matrix):
    global cnt
    if matrix[x][y] == 1:
        matrix[x][y] = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (0<=nx<n) and (0<=ny<m):
                if matrix[nx][ny] == 1:
                    cnt += 1
                    dfs(nx, ny, matrix)
    
result = []

for i in range(n):
    for j in range(m):
        cnt = 0
        dfs(i, j, matrix)
        if cnt:
            result.append(cnt+1)
print(max(result))




