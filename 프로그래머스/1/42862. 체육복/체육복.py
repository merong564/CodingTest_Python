def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    lost = set(lost)
    reserve = set(reserve)

    # 1️⃣ 자기 여벌 처리
    common = lost & reserve
    lost -= common
    reserve -= common
    
    answer = n - len(lost)
    
    for l in lost:
        # 여벌 학생이 도난당한 경우
        if l in reserve:
            answer += 1
            reserve.remove(l)
            continue
        
        # 앞 번호에게 체육복 빌림
        if l-1 in reserve:
            answer += 1
            reserve.remove(l-1)
            continue
        
        # 뒷 번호에게 체육복 빌림
        elif l+1 in reserve:
            answer += 1
            reserve.remove(l+1)
            
        
                       
    return answer