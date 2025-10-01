def solution(arr1, arr2):
    return [[c1 + c2 for c1, c2 in zip(r1, r2)] # 같은 행의 원소끼리 더함
            for r1, r2 in zip(arr1, arr2)] # 같은 행끼리 묶어서 꺼냄