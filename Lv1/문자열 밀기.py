def solution(A, B):
    answer = 0
    length = len(A)
    
    if A == B :
        return 0

    for i in range(length) :
        answer += 1
        tmp = A[-1]
        A = tmp + A[0:-1]
        if A == B :
            return answer
    
    if answer == length :
        return -1