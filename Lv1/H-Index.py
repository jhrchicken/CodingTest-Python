def solution(citations):
    answer = 0
    maxCitations = max(citations)
    lenCitations = len(citations)
    
    for h in range (maxCitations + 1) :
        cnt = 0
        for j in range (lenCitations) :
            if h <= citations[j] :
                cnt += 1
        if cnt >= h :
            answer = h
    
    return answer