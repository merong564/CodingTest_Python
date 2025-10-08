import sys

n =  int(input())

stack = []

for i in range(n):

    arr = list(sys.stdin.readline().strip().split())

    

    if len(arr) >= 2 and arr[0] == "push":

        stack.append(arr[1])

    elif arr[0] == "pop":

        if len(stack) == 0:

            print(-1)

        else:

            print(stack.pop(0))

    elif arr[0] == "size":

        print(len(stack))

    elif arr[0] == "empty":

        print(1) if len(stack) == 0 else print(0)

    elif arr[0] == "front":

        if len(stack) == 0:

            print(-1)

        else:

            print(stack[0])

    elif arr[0] == "back":

        if len(stack) == 0:

            print(-1)

        else:

            print(stack[-1])