def solution(keymap, targets):
    d={}
    for s in keymap:
        for i,c in enumerate(s,1):
            d[c]=min(d.get(c,i),i)
    return [sum(d[c] for c in t) if all(c in d for c in t) else -1 for t in targets]