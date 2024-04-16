def solution(x, n):
    answer = [x for i in range(n)]
    for i in range (n) :
        answer[i] *= (i + 1)
    return answer