def solution(my_str, n):
    answer = []
    startIdx = 0
    endIdx = n - 1
    
    length = len(my_str)
    while (startIdx < length) :
        if endIdx == length - 1 :
            answer.append(my_str[startIdx : endIdx + 1])
            break
        elif endIdx > length - 1 :
            endIdx = length - 1
        else :
            answer.append(my_str[startIdx : endIdx + 1])
            startIdx += n
            endIdx += n
    
    return answer