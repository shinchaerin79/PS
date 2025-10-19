def solution(board, moves):
    basket = []
    answer = 0

    for m in moves:
        for row in board:
            if row[m-1] != 0:
                doll = row[m-1]
                row[m-1] = 0
                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)
                break
    return answer