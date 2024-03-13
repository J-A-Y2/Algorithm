def solution(code):
    if not code:
        return "EMPTY"

    mode = 0
    ret = ""
    
    for idx, ch in enumerate(code):
        if mode == 0:
            if ch != "1" and idx % 2 == 0:
                ret += ch
            elif ch == "1":
                mode = 1
        else:
            if ch != "1" and idx % 2 == 1:
                ret += ch
            elif ch == "1":
                mode = 0
                
    return ret if ret else "EMPTY"
