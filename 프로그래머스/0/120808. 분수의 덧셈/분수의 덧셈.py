def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    for i in range(min(numer, denom)+1, 1, -1):
        if numer % i == 0 and denom % i == 0:
            numer /= i
            denom /= i
    
    # i = 2
    # while True:
    #     if i > max(numer, denom):
    #         break
    #     if numer % i == 0 and denom % i == 0:
    #         numer /= i
    #         denom /= i
    #     else:
    #         i += 1
            
    answer = [numer, denom]
    return answer