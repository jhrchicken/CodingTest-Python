def solution(emergency):
    answer = []
    
    length = len(emergency)
    for i in range(length) :
        cnt = 1
        for j in range (length) :
            if emergency[i] < emergency[j] :
                cnt += 1
        answer.append(cnt)
    
    return answer