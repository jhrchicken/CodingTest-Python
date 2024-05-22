def solution(babbling):
    answer = 0
    length = len(babbling)
    
    for i in range (length) :
        length_check = 0
        if "aya" in babbling[i] :
            length_check += 3
        if "ye" in babbling[i] :
            length_check += 2
        if "woo" in babbling[i] :
            length_check += 3
        if "ma" in babbling[i] :
            length_check += 2
        
        if length_check == len(babbling[i]) :
            answer += 1

    return answer