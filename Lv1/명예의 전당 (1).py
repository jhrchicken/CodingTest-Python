def solution(k, score):
    answer = []
    honer = []
    print(score)
    day = len(score)
    
    for i in range (day) :
        if i < k :
            honer.append(score[i])
        else :
            if score[i] > honer[k - 1] :
                honer.pop()
                honer.append(score[i])
        honer.sort(reverse=True)
        answer.append(min(honer))
    
    return answer