def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [
        sum(a == p1[i % len(p1)] for i, a in enumerate(answers)),
        sum(a == p2[i % len(p2)] for i, a in enumerate(answers)),
        sum(a == p3[i % len(p3)] for i, a in enumerate(answers)),
    ]
    m = max(scores)
    return [i+1 for i, s in enumerate(scores) if s == m]