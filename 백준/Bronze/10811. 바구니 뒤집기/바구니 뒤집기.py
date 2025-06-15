n, m = map(int, input().split())
list = list(range(1, n+1))
#print(list)

for i in range(m):
  a, b = map(int, input().split())
  
  # index 헷갈리지 않도록 1씩 빼기
  a -= 1
  b -= 1
  
  for j in range(a,b+1):
    
    # 가운데 인덱스 이후부터는 값 바꾸기 중단    
    if j >= (a+b)/2:
      break
      
    # 합이 a+b가 되는 인덱스끼리 값을 바꿈
    c = list[a+b-j]
    d = list[j]
    list[j] = c
    list[a+b-j] = d
    
    #print(list)

for i in list:
  print(i, end=' ')