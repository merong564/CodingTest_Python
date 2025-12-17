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

# 다른사람 풀이
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    