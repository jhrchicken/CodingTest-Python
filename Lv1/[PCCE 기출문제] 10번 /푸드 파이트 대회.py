def solution(food):
    answer = []
    lenFood = len(food)
    
    cnt = 1
    for i in range (1, lenFood) :
        for j in range (food[i] // 2) :
            answer.append(cnt)
        cnt += 1  
        
    answer.append(0)
    
    cnt -= 1
    for i in range (lenFood - 1, 0, -1) :
        for j in range (food[i] // 2) :
            answer.append(cnt)
        cnt -= 1
    
    return ''.join(str(x) for x in answer)