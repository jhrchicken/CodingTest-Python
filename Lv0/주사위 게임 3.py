def solution(a, b, c, d):
    answer = 0
    dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    
    dic[a] += 1
    dic[b] += 1
    dic[c] += 1
    dic[d] += 1
    print(dic)
    
    maxValue = max(dic.values())

    if maxValue == 4 :
        for i in dic :
            if dic[i] == 4 :
                return 1111 * i
    if maxValue == 3 :
        for i in dic :
            if dic[i] == 3 :
                p = i
            if dic[i] == 1 :
                q = i
        return (10 * p + q) * (10 * p + q)
    if maxValue == 2 :
        same = 1
        for i in dic :
            if dic[i] == 1 :
                same = 0
        if same == 1 :
            p = 0
            q = 0
            for i in dic :
                if dic[i] == 2 :
                    p = q
                    q = i
            print(p, q)
            return (p + q) * abs(p - q)
        else :
            q = 0
            r = 0
            for i in dic :
                if dic[i] == 1 :
                    q = r
                    r = i
            return q * r
    if maxValue == 1 :
        return min(a, b, c, d)
    
    
    
    return answer