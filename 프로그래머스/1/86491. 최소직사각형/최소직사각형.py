def solution(sizes):
    return max(max(w, h) for w, h in sizes) * max(min(w, h) for w, h in sizes)