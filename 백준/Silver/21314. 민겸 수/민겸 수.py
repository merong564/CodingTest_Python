num = input()

def find_max(num):
  cnt_m = 0
  cnt = 0
  result = ''
  
  for s in num:
    cnt += 1
    
    # M 발견할 경우
    if s == 'M':
      # 마지막 글자일 경우
      if cnt == len(num):
        result += '1'*(cnt_m+1)
      else:
        cnt_m+=1
  
    # K 발견할 경우
    if s == 'K':
      if cnt_m == 0:  # K 앞에 M이 없을 경우 K 하나가 5가 됨
        result += '5'
      else:
        result += str(5*10**cnt_m)
        cnt_m = 0  # K 발견 시 M 카운트 초기화
  
  return result

def find_min(num):
  result = ''
  cnt_m = 0
  cnt = 0
  
  for s in num:
    cnt += 1
    
    if s == 'M':
      if cnt_m == 0:
        result += '1'
      if cnt == len(num):
        result += '0'*(cnt_m)
      cnt_m += 1

    if s == 'K':
      if cnt_m >= 2:
        result += '0'*(cnt_m-1)
      result += '5'
      cnt_m = 0

  return result
max = find_max(num)
min = find_min(num)
print(max)
print(min)