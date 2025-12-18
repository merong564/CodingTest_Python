def solution(age):
    answer = ''
    # ord('a') == 97
    # ord('0') == 48
    # 0의 유니코드에 49를 더해주면 알파벳 a가 됨
    
    ## str()은 문자열로 만들기
    ## ord()는 문자를 유니코드 숫자로 변환
    ## chr()는 유니코드 숫자를 문자로 변환
    
    age_char = str(age)
    
    print('age_char: ', age_char)
    for s in age_char:
        answer += chr(ord(s) + 49)

    return answer