import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
graph = [list(map(str, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y): 
    if not visited[x][y]:
        visited[x][y] = True
        color = graph[x][y]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == color:
                    dfs(nx, ny)
        return True
    
def dfs_abnormal(x, y):    
    if not visited[x][y]:
        visited[x][y] = True
        color = graph[x][y]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if color == 'B':
                    if graph[nx][ny] == color: dfs_abnormal(nx, ny)
                elif color == 'G':
                    if (graph[nx][ny] == color) or (graph[nx][ny] == 'R'): dfs_abnormal(nx, ny)
                elif color == 'R': 
                    if (graph[nx][ny] == color) or (graph[nx][ny] == 'G'): dfs_abnormal(nx, ny)
        return True

section = 0
section_abnormal = 0
visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        result = dfs(i, j)
        if result:
            section += 1

visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        result_abnormal = dfs_abnormal(i, j)
        if result_abnormal:
            section_abnormal += 1

print(section, section_abnormal)

