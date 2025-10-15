cnt = 0

def solution(n, computers):
    global cnt
    visited = [False]*n

    for i in range(n):
        if not visited[i]:
            DFS(i, computers, visited)
            cnt += 1
        
    return cnt

def DFS(start_row, computers, visited):
    visited[start_row] = True
    
    for col in range(len(computers[start_row])): 
        if computers[start_row][col] == 1 and not visited[col]:
            DFS(col, computers, visited)         # 연결된 컴퓨터가 있으면 DFS로 방문
