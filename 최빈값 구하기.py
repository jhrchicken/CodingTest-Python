def solution(array):
    length = len(array)
    dic = dict.fromkeys(array, 0)
    
    for i in range (length) :
        dic[array[i]] += 1

    answer = array[0]
    max = dic[array[0]]
    for key in dic :
        if dic[key] > max :
            answer = key
            max = dic[key]
            
    cnt = 0
    for key in dic :
        if dic[key] == max :
            cnt += 1
    if cnt >= 2 :
        return -1
    
    return answer