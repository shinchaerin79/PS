def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for b in babbling:
        for w in words:
            if w*2 in b: break
            b = b.replace(w, ' ')
        else:
            if b.strip() == '': cnt += 1
    return cnt