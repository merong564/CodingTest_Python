import sys
sys.setrecursionlimit(10**5)

def solution(begin, target, words):
    if target not in words:
        return 0
    
    global cnt_min
    cnt_min = 9999
    
    words_dict = {}
    
    words.append(begin)

    for w in words:
        words_dict[w] = []
        
    for w in words:        
        for word in words:
            if is_one_letter_diff(w, word):
                words_dict[w].append(word)
    
    print(words_dict)
    
    visited = {key: False for key in words_dict.keys()}

    DFS(words_dict, begin, target, visited, cnt=0)
    

    if cnt_min == 9999:
        return 0
    return cnt_min


def is_one_letter_diff(w1, w2):
    diff = 0
    for c1, c2 in zip(w1, w2):
    # w1="HIT", w2="HOT"이라면 ('H','H'), ('I','O'), ('T','T') 순서대로 하나씩 꺼내어 c1과 c2에 담음
        if c1 != c2:
            diff += 1
            
    return diff == 1
        
        

def DFS(words_dict, start, target, visited, cnt):
    global cnt_min
    
    visited[start] = True
    
    for next_word in words_dict[start]:
        if visited[next_word]:
            continue
            
        if next_word == target:
            cnt += 1
            if cnt_min > cnt:
                cnt_min = cnt
                return
        else:
            DFS(words_dict, next_word, target, visited, cnt+1)
            ## 중요!! 백트래킹(방문 해제) 꼭 해줘야 함: 이걸 해줘야 A-B-C 탐색 끝나고 다시 돌아와 A-D-C 탐색할 때 방문 해제된 경로를 갈 수 있음
            visited[next_word] = False
            
            
    
    
    