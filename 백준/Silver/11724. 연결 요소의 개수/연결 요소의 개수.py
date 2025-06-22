import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v, visited, graph):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited, graph)



n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1):
    if not visited[i]:
        dfs(i, visited, graph)
        result += 1
print(result)

    