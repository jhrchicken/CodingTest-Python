def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    
    tmp = min(arr)
    for i in range (len(arr)) : 
        if arr[i] != tmp:
            answer.append(arr[i])
    return answer