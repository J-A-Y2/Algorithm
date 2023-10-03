from collections import deque

def solution(begin, target, words):
    answer = 0
    
    # target이 words 리스트 안에 없는 경우, 0을 반환
    if target not in words:
        return answer
    
    else:
    	# words의 방문 여부를 저장하는 리스트. 방문했으면 1, 아니라면 0
        visited = [0] * len(words)
        
        # 덱을 사용하여 queue를 초기화. (시작 단어, 단계) 튜플 추가
        queue = deque([(begin, answer)])
        
        while queue:
        	# 현재 단어, current까지의 단계 : 선입선출해야하므로 popleft()
            current, level = queue.popleft()
            
            # 최소 단계 찾았다면 level 반환
            if current == target:
                return level
            
            for i, word in enumerate(words):
            	# word를 방문하지 않았고, current와 다른 문자의 개수가 1개라면 ~
                if not visited[i] and sum(c1 != c2 for c1, c2 in zip(current, word)) == 1:
                    # 해당 word 방문했음 표시하고 단어와 레벨을 큐에 추가
                    visited[i] = 1
                    queue.append((word, level+1))