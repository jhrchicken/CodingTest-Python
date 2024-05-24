def solution(keymap, targets):
    answer = []
    len_keymap = len(keymap)
    len_targets = len(targets)
    
    dic_keymap = {}
    for i in range (len_keymap) :
        for j in range (len(keymap[i])) :
            if keymap[i][j] not in dic_keymap :
                dic_keymap[keymap[i][j]] = j + 1
            else :
                if dic_keymap[keymap[i][j]] > j + 1 :
                    dic_keymap[keymap[i][j]] = j + 1
    print(dic_keymap)
    
    for i in range (len_targets) :
        cnt = 0
        for j in range (len(targets[i])) :
            if targets[i][j] in dic_keymap :
                cnt += dic_keymap[targets[i][j]]
            else :
                cnt = 0
                break
        if cnt == 0 :
            answer.append(-1)
        else :
            answer.append(cnt)
    
    return answer