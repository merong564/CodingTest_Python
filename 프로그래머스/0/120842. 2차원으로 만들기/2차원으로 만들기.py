def solution(num_list, n):
    length = int(len(num_list) / n)
    answer = [[] for _ in range(length)]
    
    for i in range(length):
        answer[i] = num_list[:n]
        num_list = num_list[n:]
    
    return answer