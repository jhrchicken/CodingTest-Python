def solution(x):
    answer = False
    if x % sum(x) == 0 :
        answer = True
    return answer

def sum(num) :
    result = 0
    while (num) :
        result += int(num % 10)
        num = int(num / 10)
    return result