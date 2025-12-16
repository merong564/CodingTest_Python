def solution(array):
    max_cnt = 0
    visited = [False] * 1000
    check = 0
    
    for i in array:
        if not visited[i]:
            cnt = array.count(i)
            if cnt > max_cnt:
                max_cnt = cnt
                max_num = i
            
            elif cnt == max_cnt:
                check = i
                max_num = i
            
            visited[i] = True
        
    if max_num == check:
        return -1
    
    return max_num