def solution(rsp):
    answer = ''
    length = len(rsp)
    
    for i in range (length) :
        if (rsp[i] == '0') :
            answer += '5'
        if (rsp[i] == '2') :
            answer += '0'
        if (rsp[i] == '5') :
            answer += '2'
    
    return answer