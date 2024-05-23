def solution(num, total):
    answer = [0 for j in range(num)]
    
    # 짝수인 경우
    if num % 2 == 0 :
        answer[(num - 1) // 2] = total // num
        answer[(num + 1) // 2] = total // num + 1
        for i in range (1, num - (num // 2)) :
            answer[(num - 1) // 2 - i] = answer[(num - 1) // 2] - i
            answer[(num + 1) // 2 + i] = answer[(num + 1) // 2] + i
        print(answer)
    
    # 홀수인 경우
    else :
        answer[num // 2] = total // num
        for i in range (1, num - (num // 2)) :
            answer[num // 2 - i] = answer[num // 2] - i
            answer[num // 2 + i] = answer[num // 2] + i
    
    return answer