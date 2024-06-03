def solution(i, j, k):
    answer = 0
    for num in range (i, j + 1) :
        answer += count(num, k)
    return answer

def count (num, k) :
    cnt = 0
    while num > 0 :
        if num % 10 == k :
            cnt += 1
        num = num // 10
    return cnt