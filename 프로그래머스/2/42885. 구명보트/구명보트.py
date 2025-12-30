def solution(people, limit):
    answer = 0
    people.sort()
    
    # 가장 무거운 사람과 가장 가벼운 사람 태우기. 합이 초과한다면 무거운 사람만 태워 보내기
    start = 0
    end = len(people) - 1
    
    while start <= end:
        sum_tmp = people[start] + people[end]
        if sum_tmp <= limit:
            start += 1
                   
        end -= 1
        answer += 1
    
    # 마지막 쯤 한 명이 남거나 모두가 구조되는 경우가 있다. 전자는 세 명에서 두 명이 구조됐거나, 두 명에서 합이 초과하여 한 명만 구조된 경우이고, 후자는 두 명 또는 한 명이 남았을 때 한번에 모두 구조된 경우이다.
    # 전자의 경우 start == end인 상태로 while이 끝나므로 조건문을 통해 1 더해준다.
    # if start == end:
    #     answer += 1
    
    return answer

# 내 풀이
# def solution(people, limit):
#     answer = 0
#     weight = 0
#     cnt = 0
#     people.sort()

    
#     for p in people:
#         weight += p
#         cnt += 1
        
#         if cnt == 1:
#             if weight < limit:
#                 continue
            
#             elif weight == limit:
#                 answer += 1
#                 weight = 0
#                 cnt = 0
            
#         if cnt == 2:
#             if weight <= limit:
#                 answer += 1
#             else:
#                 answer += 2
            
#             weight = 0
#             cnt = 0
            
#     if weight != 0:
#         answer += 1
    
#     return answer