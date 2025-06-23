import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    if x<0 or x>=m or y<0 or y>=n:
        return False
    
    if not graph[x][y]:
        graph[x][y] = 1
        global cnt
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True


m, n, k = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = [[0]*n for _ in range(m)]
result = 0
cnt = 0
area = []

for _ in range(k):
    a, b, c, d= map(int, input().split())
    x1 = m-b
    y1 = a
    x2 = m-d
    y2 = c
    #print(f'x1:{x1}, y1:{y1}, x2:{x2}, y2:{y2}')
    for i in range(x2, x1):       # 범위 주의: 주어지는 것은 꼭짓점이므로, 칸의 인덱스는 그보다 1 작아야 함
        for j in range(y1, y2):
            #print('i, j: ', i, j)
            graph[i][j] = 1

for i in range(m):
    for j in range(n):
        section = dfs(i, j)
        if section:
            result += 1
            area.append(cnt)
            cnt = 0

area.sort()
print(result)
#print('area: ', area)
print(*area)
