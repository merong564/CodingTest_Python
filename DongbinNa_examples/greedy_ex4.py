## 모험가 길드: 공포도를 기준으로 그룹 최대로 나누기
# 내 풀이
# c = [0]    # 공포도별 사람 수
# g = [0]    # 공포도별 그룹 개수
# rem = [0]    # 공포도별 그룹에 포함되지 않은 사람 수

# # output
# result = 0  # 그룹의 총 개수

# # input
# n = int(input())
# x = list(map(int, input().split()))

# for i in range(1, max(x)+1):
#   c.append(x.count(i))
#   g.append((c[i] + rem[i-1]) // i)
#   rem.append((c[i] + rem[i-1]) % i)
#   result += g[i]

# print(result)

# 답안
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)
