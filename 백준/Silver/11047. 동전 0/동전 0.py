def find(k):
  global result
  if k!=0:
    for coin in coins:
        if (k-coin)>=0:
          result += k//coin
          rem = k%coin
          find(rem)
          break

n, k = map(int, input().split())
coins = []
for _ in range(n):
  coin = int(input())
  coins.append(coin)
coins.sort(reverse = True)
result = 0
find(k)
print(result)