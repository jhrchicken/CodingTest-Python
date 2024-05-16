def solution(brown, yellow):
    answer = []
    
    for i in range (1, yellow + 1) :
        if yellow % i == 0 :
            if (brown + yellow) % (i + 2) == 0 and (brown + yellow) % ((yellow / i) + 2) == 0 :
                return [(brown + yellow) / (i + 2), (i + 2)]

    return answer