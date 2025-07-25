import sys
sys.setrecursionlimit(10**5)

def find(start, end):
  global cnt
  if end < start:
    print(-1)
    sys.exit()
    
  if end%2==0:
    new_end = int(end/2)
    cnt +=1 
    # print(f'2의 배수, {end}, cnt: {cnt}')
    if new_end == start:
      return
    find(start, new_end)
    
  elif end%10==1:
    s = str(end)
    new_end = int(s[:-1])
    cnt += 1
    # print(f'끝자리 1, {end}, cnt: {cnt}')
    if new_end == start:
      return
    find(start, new_end)
    
  else:
    print(-1)
    sys.exit()

s, e = map(int, input().split())
cnt = 0
find(s, e)
print(cnt+1)

  