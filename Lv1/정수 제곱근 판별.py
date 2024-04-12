def solution(n):
    answer = -1
    root = 0
    
    for i in range(n + 1) :
        if i * i == n :
            root = i
            break
    if root != 0:
        answer = (root + 1) * (root + 1)
    return answer