def solution(n):
    town = 1
    for i in range (1, n + 1) :
        while count3times(town) == True or count3exist(town) == True :
            town += 1
            print(i, town)
        if i != n :
            town += 1
    
    return town

def count3times(num) :
    if (num % 3) == 0 :
        return True
    return False

def count3exist(num) :
    while num > 0 :
        if num % 10 == 3 :
            return True
        num = num // 10
    return False
    