def solution(numbers, hand):
    pos = {1:(0,0), 2:(0,1), 3:(0,2),
           4:(1,0), 5:(1,1), 6:(1,2),
           7:(2,0), 8:(2,1), 9:(2,2),
           '*':(3,0), 0:(3,1), '#':(3,2)}
    
    left, right = pos['*'], pos['#']
    answer = ''

    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'; left = pos[n]
        elif n in [3,6,9]:
            answer += 'R'; right = pos[n]
        else:
            l = abs(left[0]-pos[n][0]) + abs(left[1]-pos[n][1])
            r = abs(right[0]-pos[n][0]) + abs(right[1]-pos[n][1])
            if l < r or (l == r and hand == 'left'):
                answer += 'L'; left = pos[n]
            else:
                answer += 'R'; right = pos[n]
    return answer