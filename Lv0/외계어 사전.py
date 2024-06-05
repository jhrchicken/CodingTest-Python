def solution(spell, dic):
    
    for i in range(len(dic)) :
        dic_spell = dict.fromkeys(spell, 0)
        for j in range (len(dic[i])) :
            if dic[i][j] in dic_spell :
                dic_spell[dic[i][j]] += 1
                
        for k in dic_spell :
            exist = 1
            if dic_spell[k] != 1 :
                exist = 0
                break
        if exist == 1 :
            return 1

    return 2