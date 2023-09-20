def solution(answers):
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]  # 수포자들의 점수를 기록할 리스트

    # 정답과 비교하여 점수 계산
    for i in range(len(answers)):
        if answers[i] == pattern_1[i % len(pattern_1)]:
            scores[0] += 1
        if answers[i] == pattern_2[i % len(pattern_2)]:
            scores[1] += 1
        if answers[i] == pattern_3[i % len(pattern_3)]:
            scores[2] += 1

    # 가장 높은 점수를 받은 사람(들) 찾기
    max_score = max(scores)
    result = []
    for i in range(len(scores)):
        if scores[i] == max_score:
            result.append(i+1)  # 수포자 번호는 1부터 시작하므로 +1 해줌

    return result
