## 주어진 시간만큼 시간이 흐를 때 3이 나타나는 횟수
# 내 풀이
n = int(input())
result = 0

for i in range(0, n+1):
  for j in range(0, 60):
    for k in range(0, 60):
      if '3' in str(i) + str(j) + str(k):
        result += 1

print(result)
