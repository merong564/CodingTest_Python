## 체스판에서 나이트 움직이기
# 내 풀이
# s = input()

# x = int(s[1])
# y_list_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# result = 0

# x_list = [1, 2]
# y_list = [2, 1]
# sign_list = [1, -1]
# # result_array = []

# # 열 문자형 -> 정수형 변환
# for i in range(8):
#     if y_list_str[i] == s[0]:
#       y = i+1
# # print('x:{}, y:{}'.format(x,y))

# for i in range(2):
#   for j in range(2):
#     dx = x_list[i] * sign_list[j]
#     for k in range(2):
#       dy = y_list[i] * sign_list[k]

#       if 1 <= x+dx <= 8 awnd 1 <= y+dy <= 8:
#         result += 1
#         # result_array.append((x+dx, y+dy))

# print(result)
# # print(result_array)

# 답안
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
result = 0

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

for step in steps:
  x = row + step[0]
  y = column + step[1]

  if x >= 1 and x <= 8 and y >= 1 and y <= 8:
    result += 1

print(result)
