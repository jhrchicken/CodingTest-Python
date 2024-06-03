def solution(array):
    answer = 0
    for i in range (len(array)) :
        answer += count(array[i])
    return answer

def count (num) :
    cnt = 0
    while num > 0 :
        if num % 10 == 7 :
            cnt += 1
        num = num // 10
    return cnt