def solution(array):
    length = len(array)
    midean = length // 2
    array = sorted(array)
    answer = array[midean]
    return answer