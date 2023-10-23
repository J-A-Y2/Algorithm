# def solution(word):
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     answer = 0
    
#     # 각 자리수에 대한 치환 가능한 경우의 수 계산
#     weight = [781, 156, 31, 6, 1]
    
#     for i in range(len(word)):
#         answer += vowels.index(word[i]) * weight[i] + 1
    
#     return answer

# def solution(word):
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     count = 0
    
#     # 완전탐색을 위한 재귀 함수
#     def dfs(current_word, depth):
#         nonlocal count
        
#         # 주어진 단어와 일치하면 count 반환
#         if current_word == word:
#             return count
        
#         # 단어 길이가 5 이하인 경우
#         if depth < 5:
#             for v in vowels:
#                 count += 1
#                 result = dfs(current_word + v, depth + 1)
                
#                 # 주어진 단어를 찾았으면 결과 반환
#                 if result:
#                     return result
        
#         return None  # 주어진 단어가 사전에 없을 경우
    
#     return dfs('', 0)


from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(j))

    words.sort()
    return words.index(word) + 1

