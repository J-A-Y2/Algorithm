def solution(survey, choices):
    types = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    score = {type: 0 for type in types}

    for s, c in zip(survey, choices):
        if c <= 3:
            score[s[0]] += 4 - c
        elif c >= 5:
            score[s[1]] += c - 4

    result = ""
    for pair in [("R", "T"), ("C", "F"), ("M", "J"), ("A", "N")]:
        if score[pair[0]] == score[pair[1]]:
            result += min(pair)
        else:
            result += pair[0] if score[pair[0]] > score[pair[1]] else pair[1]

    return result
