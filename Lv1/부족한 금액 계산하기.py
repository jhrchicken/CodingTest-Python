def solution(price, money, count):
    sum = 0
    
    for i in range (count) :
        sum += ((i + 1) * price)
    if sum > money :
        return sum - money
    else :
        return 0