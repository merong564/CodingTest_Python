import sys
from itertools import combinations
input = sys.stdin.readline

def isit_prime(num):
    i = 2
    while True:
        if num <= i:
            return True
        if num % i == 0:
            return False
        else:
            i += 1

def solution(nums):
    global cnt
    combi_list = list(combinations(nums, 3))
    for combi in combi_list:
        sum = 0
        for i in range(3):
            sum += combi[i]
        if isit_prime(sum):
            cnt += 1
    return cnt

cnt = 0
nums = list(map(int, input().split()))
cnt = solution(nums)
print(cnt)

