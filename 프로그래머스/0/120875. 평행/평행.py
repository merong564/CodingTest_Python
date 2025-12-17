# 내 풀이 (틀림)
# 네 개의 점을 모두 사용해서 두 개씩 이어야 하기 때문에, 조합 쓰면 안됨 (문제를 잘 읽자)
from itertools import combinations

def solution(dots):
    couple_list = list(combinations(dots, 2))
    grad_list = []
    # print(couple_list)
    

    for couple in couple_list:
        a, b = couple
        grad = (b[1] - a[1]) / (b[0] - a[0])
        grad_list.append(grad)
    
    # print(grad_list)
    for grad in grad_list:
        cnt = grad_list.count(grad)
        if cnt >= 2:
            return 1
    return 0

# 답안
def solution(dots):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = dots
    
    if (y2-y1) * (x4-x3) == (y4-y3) * (x2-x1):
        return 1
    if (y4-y1) * (x3-x2) == (y3-y2) * (x4-x1):
        return 1
    if (y3-y1) * (x4-x2) == (y4-y2) * (x3-x1):
        return 1
    return 0