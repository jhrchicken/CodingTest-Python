def solution(quiz):
    answer = []
    
    lenQuiz = len(quiz)
    for i in range (lenQuiz) :
        list_quiz = quiz[i].split()
        correct = 0
        if list_quiz[1] == '+' :
            if int(list_quiz[0]) + int(list_quiz[2]) == int(list_quiz[4]) :
                correct = 1       
        else :
            if int(list_quiz[0]) - int(list_quiz[2]) == int(list_quiz[4]) :
                correct = 1
                
        if correct == 0 :
            answer.append("X")
        else :
            answer.append("O")

    return answer