import sys
input = sys.stdin.readline

def solution(k, m, score):
    rem = len(score)%m      # 박스에 들어가지 못하고 버려지는 사과 개수
    # print('rem:', rem)
    score_s = sorted(score)  # 점수 작은 순대로 정리
    # print(score_s)
    cnt = 0                 # 박스 내 사과 개수 카운트
    answer = 0

    if rem != 0:    # 버려지는 사과가 있을 경우, 점수가 낮은 사과부터 버림
        score_s = score_s[rem:]
    # print('score_s:', score_s)

    # 점수가 작은 사과끼리 박스에 넣기
    for s in score_s:
        # print('cnt:',cnt)
        if cnt == (m-1):        # 박스 내 사과 개수가 m-1이 될 때마다 0으로 초기화, answer 계산
            cnt = 0     
            answer += low * m
            # print(f'{low}를 {m}개 곱해서 {answer}가 됨')
        elif cnt == 0:
            low = s
            # print('low:', low)
            cnt += 1
        else:
            cnt += 1
    return answer

