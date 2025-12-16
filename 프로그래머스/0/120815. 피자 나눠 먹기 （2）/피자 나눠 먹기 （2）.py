def solution(n):
    for i in range(1, 100):
        if (6*i) % n == 0:
            return i