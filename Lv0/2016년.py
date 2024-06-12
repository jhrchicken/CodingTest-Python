def solution(a, b):
    answer = ''
    between = 0
    
    dic = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    for i in range (1, a) :
        between += dic[i]
    between += (b - 1)
    
    if between % 7 == 0 :
        return "FRI"
    elif between % 7 == 1 :
        return "SAT"
    elif between % 7 == 2 :
        return "SUN"
    elif between % 7 == 3 :
        return "MON"
    elif between % 7 == 4 :
        return "TUE"
    elif between % 7 == 5 :
        return "WED"
    elif between % 7 == 6 :
        return "THU"

    return answer