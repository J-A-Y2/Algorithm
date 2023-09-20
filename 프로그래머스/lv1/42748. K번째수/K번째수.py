def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        sorted_slice = sorted(array[i-1:j]) 
        k_num = sorted_slice[k-1]  # k번째 수
        answer.append(k_num)
    return answer
