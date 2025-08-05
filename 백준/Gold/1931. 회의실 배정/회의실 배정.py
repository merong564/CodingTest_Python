import sys
input = sys.stdin.readline

N = int(input())
time_arr = []

#회의 시간 입력
for _ in range(N):
    time_arr.append(tuple(map(int, input().split())))

#회의 끝나는 시간 기준으로 정렬
time_arr = sorted(time_arr, key=lambda x:(x[1], x[0]))

count = 0
last_end_time = 0

for start, end in time_arr:
    if start >= last_end_time:
        count+=1
        last_end_time = end
print(count)