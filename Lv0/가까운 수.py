def solution(array, n):
    answer = array[0]
    
    for i in range (len(array)) :
        if abs(answer - n) > abs(array[i] - n) :
            answer = array[i]
        if abs(answer - n) == abs(array[i] - n) :
            answer = min(answer, array[i])
            
    return answer