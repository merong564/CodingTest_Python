a, b, c, m = map(int, input().split())
hour = 0
tired = 0
work = 0
while True:
    if hour == 24:
        break
    if tired > m-a:
        tired -= c
        if tired < 0:
            tired = 0
    else:
        tired += a
        work += b
    hour += 1
print(work)