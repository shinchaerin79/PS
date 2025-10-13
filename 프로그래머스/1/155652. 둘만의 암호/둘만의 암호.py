def solution(s, skip, index):
    a=[c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in set(skip)]
    d={c:i for i,c in enumerate(a)}
    m=len(a)
    return ''.join(a[(d[c]+index)%m] for c in s)