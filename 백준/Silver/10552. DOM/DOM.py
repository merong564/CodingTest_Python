## 내 풀이 -> 시간 초과, hate list에서 dictionary로 변경하니 시간 초과 해결됨
# import sys
# import time

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def dfs(c, like, hate, visited):
#   global cnt
#   # 이미 방문한 채널이면 사이클 진입, -1 출력
#   if visited[c-1]:
#     cnt = 0
#     return

#   visited[c-1] = True
#   # print('current channel: ', c, end=' ')

#   for i in hate:
#     # print('i: ', i)

#     if i == c:
#       cnt += 1
#       h = hate.index(i)
#       # print('hater\'s index: ', h)
#       dfs(like[h], like, hate, visited)

#       # 현재 채널을 싫어하는 사람이 없으면 종료
#       return  

# n, m, p = map(int, input().split())

# like = [0 for _ in range(n)]
# hate = [0 for _ in range(n)]
# visited = [False]*m
# cnt = 0

# for i in range(n):
#   a, b = map(int, input().split())
#   like[i] = a
#   hate[i] = b

# # print('like: {}, hate: {}'.format(like, hate))

# dfs(p, like, hate, visited)


# if cnt == 0:
#   print(-1)
# else: print(cnt)


## 답안
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(c, visited, hate_map, like):
  global cnt
  # 이미 방문한 채널이면 사이클 진입, -1 출력
  if visited[c]:
    print(-1)
    sys.exit()

  visited[c] = True

  # 현재 채널을 싫어하는 사람이 있을 경우
  if c in hate_map:
    cnt += 1
    h = hate_map[c]  # 현재 채널을 싫어하는 사람의 
    dfs(like[h], visited, hate_map, like)


n, m, p = map(int, input().split())

like = [0]*n
hate_map = {}
visited = [False]*(m+1)
cnt = 0

for i in range(n):
  a, b = map(int, input().split())
  like[i] = a
  if b not in hate_map:
    hate_map[b] = i

dfs(p, visited, hate_map, like)
print(cnt)

## 다른 풀이
n, m, p = map(int, input().split())

hateDic = {}
visitDic = {}
visit = [0 for i in range(n)]
board = []
for i in range(n):
    loveC, hateC = map(int, input().split())
    hateP = hateDic.get(hateC, -1)
    if hateP == -1:
        hateDic[hateC] = i
    board.append([loveC, hateC])

move = 0
while True:
    hatePerson = hateDic.get(p, -1)

    if hatePerson == -1:
        print(move)
        break


    if visit[hatePerson]:
        print('-1')
        break
    else:
        visit[hatePerson] = 1
    p = board[hatePerson][0]

    move+=1
