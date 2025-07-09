from itertools import combinations

list = []
for _ in range(9):
    height = int(input())
    list.append(height)
list.sort()

for i in combinations(list, 7):
    sum = 0
    for j in i:
        sum += j
    if sum == 100:
        result = i
        break
for i in result:
    print(i)
