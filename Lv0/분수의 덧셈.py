def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = denom1 * numer2 + denom2 * numer1
    
    for i in range (2, denom + 1) :
        if denom % i == 0 and numer % i == 0 :
            denom = denom // i
            numer = numer // i
            
    for i in range (2, numer + 1) :
        if denom % i == 0 and numer % i == 0 :
            denom = denom // i
            numer = numer // i     
            
    return [numer, denom]