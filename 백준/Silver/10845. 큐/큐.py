import sys

n = int(sys.stdin.readline()) # 반복문으로 여러줄을 입력받아야 할때 input()을 사용하면, 시간초과 발생...따라서 이것을 사용

queue=[]

for i in range(n):
    Input_word = sys.stdin.readline().split()
    command = Input_word[0]

    if command == 'push':
       queue.append(Input_word[1])

    elif command == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)

    elif command == 'size':
        print(len(queue))

    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif command == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif command == 'back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])