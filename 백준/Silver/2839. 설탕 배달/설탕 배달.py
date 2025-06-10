n = int(input())

a = n // 5 
rem = n % 5

# 5로 나눈 나머지가 3으로 나누어 떨어지지 않을 경우, 5씩 더해가며 3으로 나누어 떨어지는지 확인
if rem % 3 != 0:
  
  while True:
    
    # a 가 0이 될 경우 3으로 나누어 떨어지지 않으면 -1을 출력하고 break, 나누어 떨어지면 몫만 b에 저장
    if a == 0:
      if rem % 3 != 0:
        print(-1)
        break
      else: 
        b = rem // 3
        print(a+b)
        break
      
    a -= 1
    rem += 5
    if rem % 3 == 0:
      b = rem // 3
      print(a+b)
      break
      
else: 
  b = rem // 3
  print(a+b)

