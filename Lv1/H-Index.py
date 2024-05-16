def solution(citations):
    answer = 0
    maxCitations = max(citations)
    lenCitations = len(citations)
    
    for i in range (maxCitations + 1) :
        cnt = 0
        for j in range (lenCitations) :
            if i <= citations[j] :
                cnt += 1
        if cnt >= i :
            answer = i
    
    return answer