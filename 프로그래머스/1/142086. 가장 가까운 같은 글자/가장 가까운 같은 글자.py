def solution(s):
    arr = [-1] * 26
    answer = []
    
    for i, ch in enumerate(s):
        idx = ord(ch) - ord('a')
        
        if arr[idx] == -1:
            answer.append(-1)
        else:
            answer.append(i - arr[idx])
        arr[idx] = i
    return answer
