def solution(lines):
    min = 101
    max = -101
    
    for line in lines:
        start, end = line
        if min > start:
            min = start
        if max < end:
            max = end
    
    section = [0] * (max - min)
    answer = 0
    
    for line in lines:
        start, end = line
        
        start -= min
        end -= min
            
        for i in range(start, end):
            section[i] += 1
            
    for s in section:
        if s >= 2:
            answer += 1
    
    return answer