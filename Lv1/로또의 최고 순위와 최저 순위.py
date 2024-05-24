def solution(lottos, win_nums):
    answer = []
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    cntCorrect = 0
    cntZero = 0
    for i in range (6) :
        if lottos[i] in win_nums :
            cntCorrect += 1
        if lottos[i] == 0 :
            cntZero += 1
    print(cntCorrect, cntZero)
    
    answer.append(dic[cntCorrect + cntZero])
    answer.append(dic[cntCorrect])

    return answer