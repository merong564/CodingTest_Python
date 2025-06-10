## 문자열 재정렬
# 내 풀이
# data = input()

# n = []  # 정수 리스트
# s = []  # 문자형 리스트
# result_s = []

# # print('A: ', ord('A'))
# # print('0: ', ord('0'))

# for i in range(len(data)):
#   if ord(data[i]) < 65:
#     n.append(int(data[i]))

#   else:
#     s.append(int(ord(data[i])))    # 문자형은 10진수 유니코드 값을 저장

# n.sort()
# s.sort()

# # 10진수 유니코드 -> 문자형 변환
# for i in range(len(s)):
#   result_s.append(chr(s[i]))

# for i in range(len(result_s)):
#   print(result_s[i], end='')
# for j in range(len(n)):
#   print(n[j], end='')

# 답안
data = input()
result = []
value = 0

for x in data:
  if x.isalpha():
    result.append(x)

  else:
    value += int(x)

result.sort()

if value != 0:
  result.append(str(value))

print(''.join(result))
