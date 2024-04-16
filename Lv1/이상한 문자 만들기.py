def solution(s):
    answer = []
    tmp = s.split(' ')
    
    length = len(tmp)
    for i in range (length) :
        length2 = len(tmp[i])
        for j in range (length2) :
            if j % 2 == 0 :
                answer.append(tmp[i][j].upper())
            else:
                answer.append(tmp[i][j].lower())
        if i != (length - 1) :
            answer.append(' ')

    return ''.join(answer)