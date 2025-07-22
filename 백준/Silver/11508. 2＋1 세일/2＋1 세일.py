n = int(input())
price_list = []
for _ in range(n):
  price = int(input())
  price_list.append(price)
price_list.sort(reverse=True)
result = 0
cnt = 0
for p in price_list:
  cnt += 1
  if cnt == 3:
    cnt = 0
    continue
  result += p
print(result)
  
