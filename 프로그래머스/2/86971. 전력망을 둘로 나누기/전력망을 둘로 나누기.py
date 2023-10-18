from collections import deque

# 그래프 구성
def make_graph(n, wires):
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        v1, v2 = wire
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

# DFS를 이용하여 한 쪽 전력망을 끊었을 때의 송전탑 개수 계산
def dfs(graph, node, visited):
    count = 1
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)
    return count

def solution(n, wires):
    answer = float('inf')
    graph = make_graph(n, wires)
    
    for v1, v2 in wires:
        # 한 쪽 전력망을 끊음
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        # 두 전력망의 송전탑 개수 차이 계산
        visited = [False] * (n + 1)
        count1 = dfs(graph, v1, visited)
        count2 = n - count1
        
        # 차이의 최솟값 갱신
        answer = min(answer, abs(count1 - count2))
        
        # 그래프 복원
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return answer