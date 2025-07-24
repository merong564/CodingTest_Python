# n = int(input())
# prob = input().strip()

# cnt_b = 0
# cnt_r = 0

# # B 카운팅
# before = 'R'
# for s in prob:
#   if s == 'B' and before == 'R':
#     cnt_b += 1
#   before = s

# # R 카운팅
# before = 'B'
# for s in prob:
#   if s == 'R' and before == 'B':
#     cnt_r += 1
#   before = s

# if cnt_b >= cnt_r:
#   result = cnt_r
# else:
#   result = cnt_b

# print(result+1)

## 다른 사람 답안
import sys
input = sys.stdin.readline

n = int(input())
data = input().strip()

rdata = [v for v in data.split('B') if v]
bdata = [v for v in data.split('R') if v]
result = min(len(rdata)+1, len(bdata)+1)
print(result)


    
  