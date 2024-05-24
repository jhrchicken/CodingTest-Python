def solution(s):
    answer = 0
    list = s.split()
    
    length = len(list)
    for i in range (length) :
        if list[i] == 'Z' :
            answer -= int(list[i - 1])
        else :
            answer += int(list[i])

    return answer