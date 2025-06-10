### 동빈나 3강 DFS&BFS 예제 문제

## 1. 재귀함수
def recursive_function(i):
  if i == 100:
    return

  print(i, '번째 재귀함수에서', i+1 , '번째 재귀함수를 호출합니다.')
  recursive_function(i+1)
  print(i, '번째 재귀함수를 종료합니다.')

# recursive_function(1)

## 2. DFS
graph = [
  [],
  [2, 3, 8],
  [1, 7, 8],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False]*9

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# dfs(graph, 1, visited)


## 3. BFS
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

bfs(graph, 1, visited)
