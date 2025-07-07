from collections import deque
import sys
input = sys.stdin.readline

def bfs(water, S, cnt):
    nextS = []
    nextwater = []
    for w in water:
        for i in range(4):
            x, y = w[0]+dx[i], w[1]+dy[i]
            if (0<=x<r) and (0<=y<c):       # 범위 조건이 가장 위에 와야함, 그래야 에러 안 뜸
                if matrix[x][y] == '.':
                    matrix[x][y] = cnt
                    nextwater.append([x, y])
    
    for s in S:
        for i in range(4):
            x, y = s[0]+dx[i], s[1]+dy[i]
            if (0<=x<r) and (0<=y<c):
                if [x, y] == D:
                    print(cnt)
                    return
                if matrix[x][y] == '.':
                    matrix[x][y] = 0
                    nextS.append([x, y])
    if len(nextS) == 0:
        print('KAKTUS')
    else:
        bfs(nextwater, nextS, cnt+1)
   
r, c = map(int, input().split())
matrix = []
water = []
pos = deque()
for i in range(r):
    row = list(map(str, input().strip()))
    for j in range(c):
        if row[j] == '*':
            water.append([i, j])
        if row[j] == 'D':
            D = [i, j]
        if row[j] == 'S':
            S = [[i, j]]
    matrix.append(row)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
bfs(water, S, 1)

