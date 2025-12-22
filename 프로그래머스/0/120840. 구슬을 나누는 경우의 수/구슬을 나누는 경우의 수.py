from itertools import combinations

def solution(balls, share):
    answer = factorial(balls) // (factorial(share) * factorial(balls-share))
    return answer

def factorial(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result
        