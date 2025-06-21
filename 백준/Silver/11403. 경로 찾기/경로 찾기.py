import sys
input = sys.stdin.readline

def dfs(start, node, go_list, visited):
  global result
  for i in go_list[node]:
        
    if not visited[start][i[1]]:
      #print('i in dfs: ', i)
      visited[start][i[1]] = 1
      dfs(start, i[1], go_list, visited)
      

# 입력 처리
n = int(input())
go_list = [[] for _ in range(n)]
visited = [[0]*n for _ in range(n)]
#print('visited: ', visited)

for i in range(n):
  line = list(map(int, input().split()))
  for j in range(n):
    if line[j] == 1:
      go_list[i].append((i,j))
#print('go_list: ', go_list)

for i in range(n):
  #print(f'{i}번째 사이클')
  dfs(i, i, go_list, visited)

for i in range(n):
  
  for j in range(n):
    print(visited[i][j], end=' ')
  print('')


## 다른 사람 풀이
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0]*n for _ in range(n)]

def dfs(start, cur_node, visited):
  for next_node in range(n):
    if not visited[next_node] and graph[cur_node][next_node]:
      visited[next_node] = True
      result[start][cur_node] = 1
      dfs(start, next_node, visited)

for i in range(n):
  visited = [False]*n
  dfs(i, i, visited)

for row in result:
  print(*row)
