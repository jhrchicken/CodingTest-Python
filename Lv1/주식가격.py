def solution(prices):
    answer = []
    dic_prices = {}
    lenPrices = len(prices)
    
    for i in range (lenPrices) :
        dic_prices[i] = 0
    
    for i in range (lenPrices) :
        for j in range (i + 1, lenPrices) :
            if prices[i] <= prices[j] :
                dic_prices[i] += 1
            else :
                dic_prices[i] += 1
                break
        
    for i in range (lenPrices) :
        answer.append(dic_prices[i])

    return answer