def solution(s):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i, word in enumerate(numbers):
        s = s.replace(word, str(i))
    return int(s)