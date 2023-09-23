# 입력 받기
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

# 체스판 크기가 8x8인 경우를 반복문으로 확인
min_count = float('inf')  # 최솟값 초기화
for i in range(N - 7):
    for j in range(M - 7):
        # 체스판 만들기
        chess1_count = 0  # 왼쪽 위가 흰색인 경우 칠해야 하는 개수
        chess2_count = 0  # 왼쪽 위가 검은색인 경우 칠해야 하는 개수
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y - i - j) % 2 == 0:
                    # 체스판의 색깔이 바뀌어야 하는 경우
                    if board[x][y] == 'B':
                        chess1_count += 1
                    else:
                        chess2_count += 1
                else:
                    # 체스판의 색깔이 그대로인 경우
                    if board[x][y] == 'W':
                        chess1_count += 1
                    else:
                        chess2_count += 1
        # 현재 체스판에서의 최솟값 구하기
        min_chess_count = min(chess1_count, chess2_count)
        min_count = min(min_count, min_chess_count)

# 결과 출력
print(min_count)
