def solution(a, b):
    # 연산 ⊕ 구현
    a_str = str(a)
    b_str = str(b)
    result_concatenate = int(a_str + b_str)
    
    # 2 * a * b 계산
    result_multiply = 2 * a * b
    
    # 두 결과 중 더 큰 값을 반환
    if result_concatenate >= result_multiply:
        return result_concatenate
    else:
        return result_multiply