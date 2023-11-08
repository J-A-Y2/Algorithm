def solution(triangle):
    dp = triangle
    n = len(triangle)

    for i in range(1, n):
        for j in range(i+1):
            # 왼쪽 끝인 경우
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            # 오른쪽 끝인 경우
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            # 그 외
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                
    return max(dp[n-1])
