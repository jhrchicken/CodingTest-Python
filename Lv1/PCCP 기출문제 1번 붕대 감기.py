def solution(bandage, health, attacks):
    answer = health
    
    attacks_dic = {}
    for i in range (len(attacks)) :
        attacks_dic[attacks[i][0]] = attacks[i][1]   
    
    time = attacks[-1][0]
    cast_time = 0
    for i in range (1, time + 1) :
        if i in attacks_dic :
            cast_time = 0
            answer -= attacks_dic[i]
        else :
            cast_time += 1
            if cast_time == bandage[0] :
                answer += bandage[2]
                cast_time = 0
            answer += bandage[1]
            if (answer + bandage[1]) > health :
                answer = health
                
        if answer <= 0 :
            return -1
    
    return answer