def solution(numlist, n):
    answer = []
    
    while (len(numlist)) :
        min = abs(numlist[0] - n)
        min_idx = 0
        for i in range (len(numlist)) :
            if (min > abs(numlist[i] - n)) :
                min = abs(numlist[i] - n)
                min_idx = i
            if (min == abs(numlist[i] - n)) :
                if (numlist[min_idx] < numlist[i]) :
                    min_idx = i
        answer.append(numlist[min_idx])
        del numlist[min_idx]
        
    return answer