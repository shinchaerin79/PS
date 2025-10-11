from itertools import combinations

def solution(nums):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True
    return sum(is_prime(sum(c)) for c in combinations(nums, 3))