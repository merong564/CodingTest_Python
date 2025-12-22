def solution(numbers, direction):
    if direction == 'left':
        answer = numbers[1:]
        answer.append(numbers[0])
    else:
        answer = [numbers[-1]]
        answer.extend(numbers[:-1])
    return answer