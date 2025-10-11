def solution(N, stages):
    result = []
    total = len(stages)
    for i in range(1, N+1):
        cnt = stages.count(i)
        fail = cnt / total if total else 0
        result.append((i, fail))
        total -= cnt
    return [x[0] for x in sorted(result, key=lambda x: (-x[1], x[0]))]