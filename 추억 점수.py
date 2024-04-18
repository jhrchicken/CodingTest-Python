def solution(name, yearning, photo):
    answer = []
    
    lenPhoto = len(photo)
    for i in range(lenPhoto) :
        sum = 0
        lenPhotoDeep = len(photo[i])
        for j in range (lenPhotoDeep) :
            lenName = len(name)
            for k in range (lenName) :
                if photo[i][j] == name[k] :
                    sum += yearning[k]
        answer.append(sum)
        
    return answer