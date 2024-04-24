def solution(cards1, cards2, goal):
    idx1 = 0
    idx2 = 0
    len1 = len(cards1)
    len2 = len(cards2)
    
    length = len(goal)
    for i in range (length) :
        if (len1 > idx1) and (goal[i] == cards1[idx1]) :
                idx1 += 1
        elif (len2 > idx2) and (goal[i] == cards2[idx2]) :
                idx2 += 1
        else :
            return "No"
    return "Yes"