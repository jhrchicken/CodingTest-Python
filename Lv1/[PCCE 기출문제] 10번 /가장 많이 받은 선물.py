def solution(friends, gifts):  
    point = dict.fromkeys(friends, 0)
    nextMonth = dict.fromkeys(friends, 0)
    
    # 선물지수 구하기
    lenGifts = len(gifts)
    for i in range (lenGifts) :
        listGifts = gifts[i].split()
        point[listGifts[0]] += 1
        point[listGifts[1]] -= 1
        
    # 친구별 선물 수 구하기
    lenFriends = len(friends)
    for i in range (lenFriends) :
        exchange = dict.fromkeys(friends, 0)
        for j in range (lenGifts) :
            listGifts = gifts[j].split()
            if (listGifts[0] == friends[i]) :
                exchange[listGifts[1]] -= 1
            if (listGifts[1] == friends[i]) :
                exchange[listGifts[0]] += 1
        print(exchange)
        
        # 받을 선물 수 구하기
        for j in range (lenFriends) :
            if exchange[friends[i]] > exchange[friends[j]] :
                nextMonth[friends[i]] += 1
            if exchange[friends[i]] == exchange[friends[j]] :
                if point[friends[i]] > point[friends[j]] :
                    nextMonth[friends[i]] += 1
        # print(nextMonth)
    
    # 받은 선물의 최대값 찾기
    max = 0
    for i in range (lenFriends) :
        if max < nextMonth[friends[i]] :
            max = nextMonth[friends[i]]
    
    return max