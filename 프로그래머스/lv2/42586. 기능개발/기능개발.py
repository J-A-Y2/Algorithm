# 100을 기준으로 봤을때, 100 - progress 는 남은 작업이고 여기에 스피드를 나누면 배포일수가 나온다.
# 배포일수를 기준으로 배열를 만들고 앞에 배열이 뒤의 배열들 보다 크거나 같으면 카운트를 하고 뒤의 값이 커지는 순간 카운트를 리턴하고 다시 앞의 과정을 진행하면 될 것 같다.
#아니 근데 이미 백분율 비율이 다 통일인데 그냥 프로그래스랑 스피드 100 될때까지 더해서 첫번째 값이 100이 될때 100 인 숫자들 카운트 하면 될것같은데... 
# import math

def solution(progresses, speeds):
    stack = []
    
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        count = 0
        
        while progresses and 100 <= progresses[0]:
            count += 1
            del progresses[0]
            del speeds[0]
        
        if count != 0:
            stack.append(count)
            
    return stack        

# import math   
# from collections import deque

# def solution(progresses, speeds):
#     deploy_count = []  # 배포되는 작업의 수를 저장할 리스트
#     queue = deque()

#     for progress, speed in zip(progresses, speeds):
#         deploy_day = math.ceil((100 - progress) / speed)  # 배포까지 걸리는 일수 계산
#         queue.append(deploy_day)  # 일수를 큐에 추가

#     while queue:
#         deploy_day = queue.popleft()
#         count = 1  # 배포되는 작업의 수
#         # 큐의 원소와 비교하여 배포 가능한 작업 수 계산
#         while queue and queue[0] <= deploy_day:
#             queue.popleft()
#             count += 1
#         deploy_count.append(count)  # 배포되는 작업의 수를 결과 리스트에 추가

#     return deploy_count
