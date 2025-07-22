import sys

def find(n):
  global coins
  if n < 0:
    print(-1)
    sys.exit()
    
  if n % 5 == 0:
    coins += n//5

  else:
    n -= 2
    coins += 1
    find(n)

n = int(input())
coins = 0
find(n)
print(coins)

    
  