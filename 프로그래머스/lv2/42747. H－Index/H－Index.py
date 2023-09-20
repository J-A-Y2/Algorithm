def solution(citations):
    citations.sort(reverse=True)  # 인용 횟수를 내림차순으로 정렬
    h_index = 0

    for i in range(len(citations)):
        if citations[i] >= i + 1:  # 현재 논문의 인용 횟수가 현재 인덱스보다 크거나 같을 때
            h_index = i + 1

    return h_index
