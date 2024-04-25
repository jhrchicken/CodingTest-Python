def solution(data, ext, val_ext, sort_by):
    answer = []
    dic = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    
    lenData = len(data)
    for i in range (lenData) :
        if data[i][dic[ext]] < val_ext :
            answer.append(data[i])
    print(answer)
    
    lenAnswer = len(answer)
    for i in range(lenAnswer) :
        for j in range (i) :
            if answer[i][dic[sort_by]] < answer[j][dic[sort_by]] :
                tmp = answer[i]
                answer[i] = answer[j]
                answer[j] = tmp
    
    print(answer)
    return answer