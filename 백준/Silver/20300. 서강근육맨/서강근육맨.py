import sys
input = sys.stdin.readline

def find_min(mus_list):
  global max_sum
  if n%2 == 0:    # n이 짝수일 경우
    for i in range(int(len(mus_list)/2)):
      sum = mus_list[i] + mus_list[-(i+1)]
      max_sum = max(sum, max_sum)
  else:          # n이 홀수일 경우
    new_mus_list = mus_list[:-1]
    for i in range(int(len(new_mus_list)/2)):
      sum = new_mus_list[i] + new_mus_list[-(i+1)]
      max_sum = max(sum, max_sum)

n = int(input())
mus = list(map(int, input().split()))
mus.sort()
max_sum = 0
find_min(mus)
print(max_sum)


    
    
  