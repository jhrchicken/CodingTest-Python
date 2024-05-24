def solution(lines):
    answer = 0
    dic = {}
    
    max = lines[0][0]
    min = lines[0][0]
    for i in range (3) :
        for j in range (2) :
            if max < lines[i][j] :
                max = lines[i][j]
            if min > lines[i][j] :
                min = lines[i][j]

    print(min, max)
    for i in range (min, max + 1) :
        dic[i] = 0
    
    for i in range (lines[0][0], lines[0][1]) :
        dic[i] += 1
    for i in range (lines[1][0], lines[1][1]) :
        dic[i] += 1
    for i in range (lines[2][0], lines[2][1]) :
        dic[i] += 1
    
    for i in dic :
        if dic[i] > 1 :
            answer += 1
    
    return answer