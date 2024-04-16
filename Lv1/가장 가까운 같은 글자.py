def solution(s):
    length = len(s)
    answer = [-1 for i in range (length)]
    
    for i in range (length) :
        for j in range (i) :
            if s[i] == s[j] :
                answer[i] = i - j
    print(answer)
    
    return answer