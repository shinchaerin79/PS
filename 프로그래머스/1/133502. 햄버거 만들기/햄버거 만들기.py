def solution(ingredient):
    s = []
    cnt = 0
    for x in ingredient:
        s.append(x)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            del s[-4:]
    return cnt