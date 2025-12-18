def solution(num, total):
    answer = []
    sum = 0
    for i in range(1, num):
        sum += i
        
    first_num = (total - sum) / num
    
    for i in range(num):
        answer.append(first_num+i)
        
    return answer
