def solution(phone_number):
    answer = ''
    length = len(phone_number)
    for i in range(length) :
        if (i < length - 4) :
            answer += "*"
        else :
            answer += phone_number[i]
    return answer