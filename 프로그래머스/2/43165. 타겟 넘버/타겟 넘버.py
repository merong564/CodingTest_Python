cnt = 0
def solution(numbers, target):
    global cnt
    
    DFS(numbers, target, 0, 0)
    
    return cnt

def DFS(numbers, target, sum, idx):
    global cnt
    operators = ['+', '-']
    # print(f'idx: {idx}, sum: {sum}')
    
    if idx == len(numbers):
        # print(f'마지막 인덱스 도착, 계: {sum}')
        if sum == target:
            cnt += 1
        return
    
    for oper in operators:
        if oper == '+':
            DFS(numbers, target, sum+numbers[idx], idx+1)
        else:
            DFS(numbers, target, sum-numbers[idx], idx+1)
            
        