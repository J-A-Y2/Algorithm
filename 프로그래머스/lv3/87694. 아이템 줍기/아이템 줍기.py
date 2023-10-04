# from collections import deque
# import copy


# def adjacent_nodes(x, y, field, visited):
#     adjacent = []
#     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         nx, ny = x + dx, y + dy
#         if (
#             0 <= nx < len(field)
#             and 0 <= ny < len(field[0])
#             and visited[nx][ny] == 0
#             and field[nx][ny] == 1
#         ):
#             adjacent.append((nx, ny))
#     return adjacent


# def bfs(characterX, characterY, itemX, itemY, field, visited):
#     q = deque()
#     q.append([characterX, characterY, 0])
#     distance = 0
#     visited[characterX][characterY] = 1

#     while q:
#         x, y, distance = q.popleft()
#         if x == itemX and y == itemY:
#             return distance // 2

#         for i, j in adjacent_nodes(x, y, field, visited):
#             if visited[i][j] == 0 and field[i][j] == 1:
#                 visited[i][j] = 1
#                 distance += 1
#                 q.append((i, j, distance))


# def solution(rectangle, characterX, characterY, itemX, itemY):
#     new_rectangle = []
#     for i in rectangle:
#         new_rectangle.append(list(map(lambda x: x * 2, i)))

#     characterX *= 2
#     characterY *= 2
#     itemX *= 2
#     itemY *= 2
    
#     max_x = 0
#     max_y = 0
#     for x1, y1, x2, y2 in new_rectangle:
#         max_x = max(max_x, x1, x2)  # 행
#         max_y = max(max_y, y1, y2)  # 열

#     # 0,0에서 시작이 아니므로 x,y좌표 1씩 늘려줌
#     visited = [[0 for _ in range(max_y + 1)] for _ in range(max_x + 1)]

#     # visited를 깊은 복사로 완전 새롭게 복사함
#     field = copy.deepcopy(visited)

#     # 사각형 외각선 모두 1로 표현
#     for i in range(len(new_rectangle)):
#         x1 = new_rectangle[i][0]
#         y1 = new_rectangle[i][1]
#         x2 = new_rectangle[i][2]
#         y2 = new_rectangle[i][3]
#         for x in range(x1, x2 + 1):
#             field[x][y1] = 1
#             field[x][y2] = 1
#         for y in range(y1, y2 + 1):
#             field[x1][y] = 1
#             field[x2][y] = 1

#     # 사각형 내부에 있는 1을 0으로 바꿈
#     for i in range(len(new_rectangle)):
#         x1 = new_rectangle[i][0]
#         y1 = new_rectangle[i][1]
#         x2 = new_rectangle[i][2]
#         y2 = new_rectangle[i][3]
#         for x in range(x1 + 1, x2):
#             for y in range(y1 + 1, y2):
#                 field[x][y] = 0

#     return bfs(characterX, characterY, itemX, itemY, field, visited)

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0 
    field = [[-1] * 102 for i in range(102)]
    for r in rectangle:
        x1 = r[0] * 2
        y1 = r[1] * 2
        x2 = r[2] * 2
        y2 = r[3] * 2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:    
                    field[i][j] = 1

    dx = [0, 0, -1, 1]  
    dy = [1, -1, 0, 0]  
    q = deque()
    q.append([characterX * 2, characterY * 2])   
    visited = [[1] * 102 for i in range(102)]  
    while q:    
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        for k in range(4):
            nx = x + dx[k] 
            ny = y + dy[k] 
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1   
    return answer