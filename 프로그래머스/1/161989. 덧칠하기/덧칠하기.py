def solution(n, m, section):
    cnt = 0; end = 0
    for s in section:
        if s > end:
            cnt += 1
            end = s + m - 1
    return cnt