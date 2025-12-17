n = int(input())
answer = ''
for i in range(1, n+1):
    if i == 1:
        answer += '*'
    else:
        answer += '\n' + '*' * i
print(answer)