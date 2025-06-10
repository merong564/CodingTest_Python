n, k = map(int,(input().split()))
cnt = 0

while True:
  num = (n // k) * k  # k로 나눠지는 가장 큰 수
  cnt += n - num    # num이 될 때까지 1씩 뺀 횟수 카운트

  if n < k:    # n을 k로 더 나눌 수 없을 때 반복문 탈출
    cnt += n-1    # 1이 될 때까지 뺀 횟수 카운트
    break
    
  n = num // k   # num에서 k로 나눈 몫을 n에 대입
  cnt += 1      # 나눈 횟수 카운트
  

cnt -= 1  # if문 전에 cnt += 1이 되므로 1을 빼줌
print(cnt)
