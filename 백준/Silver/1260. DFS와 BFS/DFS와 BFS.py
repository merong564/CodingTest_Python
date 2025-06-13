from collections import deque

n, m, v = map(int, input().split())
graph = [
  []
]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

for i in range(n):
  graph.append([])

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  graph[a].sort()
  graph[b].sort()

# print(graph)

def dfs(graph, v, visited):
  print(v, end=' ')
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
      

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  
  while queue:
    k = queue.popleft()
    print(k, end=' ')
    
    for i in graph[k]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        
dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)
    
