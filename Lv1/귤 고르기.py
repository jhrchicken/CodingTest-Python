def solution(k, tangerine):
    answer = 0
    dic = {}
    lenTgr = len(tangerine)
    
    for i in range (lenTgr) :
        if tangerine[i] in dic :
            dic[tangerine[i]] += 1
        else :
            dic[tangerine[i]] = 1
    
    tangerine_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    for i in range (lenTgr) :
        answer += 1
        k -= tangerine_list[i][1]
        if k <= 0 :
            return answer