def solution(num, total):
    answer = []
    sum = 0
    for i in range(1, num+1):
        sum += i
        
    first_num = (total - sum) / num + 1
    
    for i in range(num):
        answer.append(first_num+i)
        
    return answer