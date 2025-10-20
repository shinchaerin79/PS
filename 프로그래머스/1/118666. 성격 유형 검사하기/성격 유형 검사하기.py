def solution(survey, choices):
    score = {ch: 0 for ch in "RTCFJMAN"}
    point = [3, 2, 1, 0, 1, 2, 3]

    for s, c in zip(survey, choices):
        if c < 4:
            score[s[0]] += point[c - 1]
        elif c > 4:
            score[s[1]] += point[c - 1]

    return ''.join([
        'R' if score['R'] >= score['T'] else 'T',
        'C' if score['C'] >= score['F'] else 'F',
        'J' if score['J'] >= score['M'] else 'M',
        'A' if score['A'] >= score['N'] else 'N'
    ])