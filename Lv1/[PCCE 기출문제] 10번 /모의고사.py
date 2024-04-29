def solution(answers):
    giveUp1 = [1,2,3,4,5]
    giveUp2 = [2,1,2,3,2,4,2,5]
    giveUp3 = [3,3,1,1,2,2,4,4,5,5]
    correct = [0,0,0]
    answer = []
    
    lenAnswers = len(answers)
    for i in range (lenAnswers) :
        if (answers[i] == giveUp1[(i % 5)]) :
            correct[0] += 1
        if (answers[i] == giveUp2[(i % 8)]) :
            correct[1] += 1
        if (answers[i] == giveUp3[(i % 10)]) :
            correct[2] += 1
    
    maxCorrect = max(correct)
    for i in range (3) :
        if correct[i] == maxCorrect :
            answer.append(i + 1)
        
    return answer