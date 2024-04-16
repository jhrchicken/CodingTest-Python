def solution(number):
    answer = 0
    
    for i in range (2, len(number)) :
        for j in range (1, i) :
            for k in range (j) :
                if number[i] + number[j] + number[k] == 0 :
                    answer += 1
    return answer