def solution(emergency):
    answer = []
    emergency_sorted = sorted(emergency, reverse=True)
    
    for num in emergency:
        answer.append(emergency_sorted.index(num) + 1)
        
    return answer