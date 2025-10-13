def solution(lottos, win_nums):
    r=lambda x:6 if x<2 else 7-x
    m=len(set(lottos)&set(win_nums))
    z=lottos.count(0)
    return [r(m+z),r(m)]