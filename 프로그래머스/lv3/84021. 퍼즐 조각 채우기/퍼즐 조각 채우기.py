from collections import deque
import copy

# 상, 하, 좌, 우 방향 이동을 위한 상대 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
empty_g = []
block_t = []

def bfs(x, y, N, visited, array, check):
    space = []
    que = deque()
    que.append([x, y])
    space.append([x, y])
    visited[x][y] = True

    while que:
        px, py = que.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny] is False and array[nx][ny] == check:
                visited[nx][ny] = True
                que.append([nx, ny])
                space.append([nx, ny])

    return sorted(space)

def rotate(b, N):
    new_board = []
    for block in b:
        new_board.append([block[1], N - 1 - block[0]])
    return sorted(standard(new_board, N))

def standard(b, N):
    change = []
    minx = N
    miny = N

    for i in b:
        minx = min(minx, i[0])
        miny = min(miny, i[1])
    for x, y in b:
        change.append([x - minx, y - miny])
    return sorted(change)

def solution(game_board, table):
    global answer
    answer = 0
    N = len(game_board)

    visited_g = [[False for _ in range(N)] for _ in range(N)]
    visited_t = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0 and visited_g[i][j] is False:
                empty_g.append(bfs(i, j, N, visited_g, game_board, 0))
            if table[i][j] == 1 and visited_t[i][j] is False:
                block_t.append(bfs(i, j, N, visited_t, table, 1))
            else:
                continue

    table_block = []
    for a in block_t:
        table_block.append(standard(a, N))

    game_block = []
    for b in empty_g:
        game_block.append(standard(b, N))

    for g_block in game_block:
        if g_block in table_block:
            answer += len(g_block)
            table_block.remove(g_block)
        else:
            flag = False
            for t_block in table_block:
                temp = copy.copy(t_block)
                for z in range(4):
                    if g_block == temp:
                        answer += len(g_block)
                        table_block.remove(t_block)
                        flag = True
                        break
                    temp = rotate(temp, N)
                if flag:
                    break
    return answer


# from collections import deque

# # 상, 하, 좌, 우 방향 이동을 위한 상대 좌표
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # 퍼즐 조각의 모양을 저장하기 위한 리스트 생성
# def get_piece(shape):
#     piece = []
#     min_row, min_col = float('inf'), float('inf')
#     for i, j in shape:
#         piece.append((i, j))
#         min_row = min(min_row, i)
#         min_col = min(min_col, j)
#     # 모양을 정규화하여 좌상단을 (0,0)으로 만듭니다.
#     normalized_piece = []
#     for i, j in piece:
#         normalized_piece.append((i - min_row, j - min_col))
#     return normalized_piece

# # 게임 보드와 퍼즐 조각의 상태를 그래프로 나타내는 함수
# def get_graph(board):
#     n = len(board)
#     graph = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == 1:
#                 continue
#             if graph[i][j] == 0:
#                 shape = []
#                 queue = deque([(i, j)])
#                 while queue:
#                     x, y = queue.popleft()
#                     shape.append((x, y))
#                     graph[x][y] = 1
#                     for k in range(4):
#                         nx, ny = x + dx[k], y + dy[k]
#                         if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and graph[nx][ny] == 0:
#                             queue.append((nx, ny))
#                 yield get_piece(shape)

# # BFS 탐색을 통해 매칭 가능한 퍼즐을 찾는 함수
# def find_match(board, piece):
#     n = len(board)
#     visited = [[False] * n for _ in range(n)]
#     queue = deque([(0, 0)])
#     while queue:
#         x, y = queue.popleft()
#         if visited[x][y]:
#             continue
#         visited[x][y] = True
#         for k in range(4):
#             nx, ny = x + dx[k], y + dy[k]
#             if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#                 if piece[nx][ny] == 1:
#                     return False
#                 if board[nx][ny] == 0:
#                     queue.append((nx, ny))
#     return True

# def solution(game_board, table):
#     # 게임 보드와 테이블을 그래프로 변환
#     game_board_graph = list(get_graph(game_board))
#     table_graph = list(get_graph(table))

#     # 테이블의 퍼즐을 하나씩 꺼내서 게임 보드와 매칭 가능한지 확인
#     matched_count = 0
#     for piece in table_graph:
#         for i in range(len(game_board_graph)):
#             if len(piece) != len(game_board_graph[i]):
#                 continue
#             if find_match(game_board_graph[i], piece):
#                 matched_count += len(piece)
#                 game_board_graph.pop(i)
#                 break

#     return matched_count

# # # 예제 입력
# # game_board = [[1, 1, 0], [1, 0, 0], [0, 0, 1]]
# # table = [[1, 1, 0], [1, 0, 0], [0, 0, 1]]

# # # 결과 출력
# # print(solution(game_board, table))  # 출력: 14
