def solution(survey, choices):
    # 각 성격 유형에 따른 점수를 저장할 딕셔너리 초기화
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    # survey와 choices 배열을 동시에 순회하면서 점수 계산
    for i in range(len(survey)):
        if choices[i] <= 3:  # '매우 비동의', '비동의', '약간 비동의'
            score[survey[i][0]] += 4 - choices[i]
        elif choices[i] >= 5:  # '약간 동의', '동의', '매우 동의'
            score[survey[i][1]] += choices[i] - 4

    # 각 지표별로 더 높은 점수를 가진 성격 유형 결정
    result = ""
    for pair in [("R", "T"), ("C", "F"), ("M", "J"), ("A", "N")]:
        if score[pair[0]] > score[pair[1]]:
            result += pair[0]
        elif score[pair[0]] < score[pair[1]]:
            result += pair[1]
        else:  # 점수가 같을 경우 사전 순으로 빠른 성격 유형 선택
            result += min(pair)

    return result
