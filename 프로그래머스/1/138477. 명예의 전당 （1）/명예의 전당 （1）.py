def solution(k, score):
    result = []
    honor = []
    for s in score:
        honor.append(s)
        honor.sort(reverse=True)
        if len(honor) > k:
            honor.pop()
        result.append(honor[-1])
    return result