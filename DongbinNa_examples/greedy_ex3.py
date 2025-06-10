## 곱하거나 더해서 가장 큰 수 만들기
# 내 풀이
# s = input()
# n = len(s)
# sum = int(s[0])

# for i in range(1, n):
#   if s[i - 1] == '1' or s[i - 1] == '0' or s[i] == '1' or s[i] == '0':
#     sum += int(s[i])
#   else:
#     sum *= int(s[i])

# print(sum)

# 답안
s = input()
result = int(s[0])

for i in range(1, len(s)):
  num = int(s[i])
  if result <= 1 or num <= 1:
    result += num
  else:
    result *= num

print(result)
