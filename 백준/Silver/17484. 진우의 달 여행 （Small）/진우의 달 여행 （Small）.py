def find(start, fuel, before):
    x, y = start
    if x == n-1:
        return fuel
    min_fuel = float('inf')
    for i in range(3):
        if i != before:
            nx = x+dx[i]
            ny = y+dy[i]
            if (0<=nx<n) and (0<=ny<m):
                total = find((nx, ny), fuel+matrix[nx][ny], i)
                min_fuel = min(min_fuel, total)
    return min_fuel

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

dx = [1, 1, 1]
dy = [-1, 0, 1]
result = []

for i in range(m):
    fuel = find((0, i), matrix[0][i], 100)
    # print(f'(0,{i}) 시작할 때 result: ', result)
    result.append(fuel)

# print(result_list)
print(min(result))


