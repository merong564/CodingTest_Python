import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(start, cnt, visited):    
    if cnt == 4:
        print(1)
        sys.exit()
    visited[start] = True
    for friend in graph[start]:
        if not visited[friend]:            
            dfs(friend, cnt+1, visited)
    visited[start] = False      # !! 중요 !! 방문처리를 끝내줘야 다른 경로 찾을 때 문제 없음


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for start in range(n):
    visited = [False]*n
    cnt = 0
    visited[start] = True
    dfs(start, cnt, visited)

print(0)