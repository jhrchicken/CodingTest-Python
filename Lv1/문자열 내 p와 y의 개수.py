def solution(s):
    answer = True
    cntP = 0
    cntY = 0
    
    s = s.lower()
    for i in range(len(s)):
        if s[i] == 'p' :
            cntP += 1
        if s[i] == 'y' :
            cntY += 1
    
    if cntP != cntY :
        answer = False
    
    return answer