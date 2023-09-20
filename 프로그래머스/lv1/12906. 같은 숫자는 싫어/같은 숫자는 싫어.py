def solution(arr):
    ans = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            ans.append(arr[i])
    return ans

# from collections import deque

# def solution(arr):
#     stack = deque()
#     for num in arr:
#         if len(stack) == 0 or num != stack[-1]:
#             stack.append(num)
#     return list(stack)
