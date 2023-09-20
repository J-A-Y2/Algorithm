#괄호를 올바르게 열고 닫는것을 확인하는 문제. 괄호로만 이루어진 입력값이 주어졌을때, 올바른 괄호이면 true 아니면 false를 return 해야함. 
# 괄호 방향을 1, -1 로 생각하면 짝지어진 괄호의 총합은 항상 0이 되니까 괄호를 숫자로 지정해서 계산하면 되겠다. 맞나? 음...  3번째 예시도 0인데? 아 -1로 시작하면 무조건 false로 return 하자

def solution(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0


# answer_dict = {"(" : 1, ")" : -1}
# def solution(s):
#     current_value = 0
#     for i in s :
#         current_value += answer_dict[i]
#         if current_value < 0:
#             return False
#     return True if current_value == 0 else False

# from collections import deque

# def solution(s):
#     stack = deque()
#     for char in s:
#         if char == '(':
#             stack.append(char)
#         elif char == ')':
#             if len(stack) > 0 and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0
