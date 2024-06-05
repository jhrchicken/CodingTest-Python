def solution(score):
    avg = []
    answer = []
    
    for i in range (len(score)) :
        avg.append((score[i][0] + score[i][1]) / 2)
    
    for i in range (len(avg)) :
        grade = 1
        for j in range (len(avg)) :
            if avg[i] < avg[j] :
                grade += 1
        answer.append(grade)
    
    return answer