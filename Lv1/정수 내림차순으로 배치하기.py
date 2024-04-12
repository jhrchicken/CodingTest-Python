def solution(n):
    answer = 0
    list_n = []
    
    while n > 0:
        list_n.append(int(n % 10))
        n = int(n / 10)
        
    list_n.sort()
    print(list_n)
    
    for i in range (len(list_n) -1, -1, -1) :
        answer = answer * 10 + list_n[i]
    return answer