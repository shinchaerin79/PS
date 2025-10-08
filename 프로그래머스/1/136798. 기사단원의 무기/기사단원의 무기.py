def solution(number, limit, power):
    cnt = [0]*(number+1)
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            cnt[j] += 1
    return sum(c if c <= limit else power for c in cnt[1:])