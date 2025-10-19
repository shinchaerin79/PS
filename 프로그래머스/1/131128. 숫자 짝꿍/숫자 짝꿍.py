from collections import Counter

def solution(X, Y):
    x_count = Counter(X)
    y_count = Counter(Y)
    
    common = []
    for num in (set(X) & set(Y)):
        count = min(x_count[num], y_count[num])
        common.extend([num] * count)
    
    if not common:
        return "-1"
    
    answer = ''.join(sorted(common, reverse=True))
    if answer[0] == '0':
        return "0"
    
    return answer