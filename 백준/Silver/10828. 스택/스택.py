import sys

n = int(sys.stdin.readline()) # 반복문으로 여러줄을 입력받아야 할때 input()을 사용하면, 시간초과 발생...따라서 이것을 사용

stack=[]

for i in range(n):
    Input_word = sys.stdin.readline().split()
    command = Input_word[0]

    if command == 'push':
        value = Input_word[1]
        stack.append(value)

    elif command == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    elif command == 'size':
        print(len(stack))

    elif command == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    elif command == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])