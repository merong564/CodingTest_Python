n = int(input())
t = list(map(int, input().split()))

result = 0

t.sort()

for i in range(1, n+1):
  for j in range(i):
    result += t[j]
  
print(result)
