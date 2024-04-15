def solution(left, right):
    answer = 0
    for i in range (left, right + 1) :
        if oddEven(i) == 1 :
            answer += i
        else :
            answer -= i
    return answer

def oddEven(num) :
    cnt = 0
    for i in range(num) :
        if num % (i + 1) == 0 :
            cnt += 1
    if cnt % 2 == 0 :
        return 1
    return 0