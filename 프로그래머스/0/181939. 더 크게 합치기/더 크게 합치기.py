def concatenate(a, b):
    # 두 정수를 문자열로 변환하여 이어붙인 후 정수로 변환하여 반환합니다.
    return int(str(a) + str(b))

def solution(a, b):
    # a ⊕ b 계산 결과
    result1 = concatenate(a, b)
    # b ⊕ a 계산 결과
    result2 = concatenate(b, a)

    # 더 큰 값을 반환합니다.
    return max(result1, result2)