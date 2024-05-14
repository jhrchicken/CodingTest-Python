def solution(n):
    answer = 0
    base3 = 0
    
    while n > 0 :
        base3 = base3 * 10 + (n % 3)
        n = n // 3
    print(base3)

    i = 0
    while base3 > 0 :
        digit = 1
        for j in range (i) :
            digit *= 3
        answer += (base3 % 10) * digit
        base3 = base3 // 10
        i += 1

    
    
    return answer