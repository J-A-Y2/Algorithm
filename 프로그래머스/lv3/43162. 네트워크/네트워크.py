def dfs(computers, visited, i):
    visited[i] = True  # 현재 컴퓨터 방문 체크
    
    for j in range(len(computers)):
        if computers[i][j] == 1 and not visited[j]:  # i번 컴퓨터와 연결되어 있고, 아직 방문하지 않은 컴퓨터라면
            dfs(computers, visited, j)  # 해당 컴퓨터로 DFS 탐색

def solution(n, computers):
    answer = 0
    visited = [False] * n  # 컴퓨터 방문 여부를 나타내는 리스트
    
    for i in range(n):
        if visited[i] == False:  # 아직 방문하지 않은 컴퓨터라면
            dfs(computers, visited, i)  # DFS 탐색 수행
            answer += 1  # 네트워크 개수 증가
    
    return answer
