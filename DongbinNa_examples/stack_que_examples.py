### 동빈나 3강 자료형 구현 예제

## 1. stack 자료형
stack = []
stack.append(5)
stack.append(3)
stack.append(4)
stack.pop()  # 가장 오른쪽(최근) 원소를 빼기
stack.append(1)

print(stack[::-1])  # 최상단 원소부터 출력
print(stack)

## 2. que 자료형
from collections import deque

queue = deque()

queue.append(5)
queue.append(3)
queue.append(2)
queue.popleft()  # 가장 오래된 원소를 빼기
queue.append(0)
queue.append(1)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
