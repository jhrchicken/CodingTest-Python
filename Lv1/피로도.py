import itertools

def solution(k, dungeons):
    maxCnt = 0
    
    dungeonsList = list(itertools.permutations(dungeons))

    lenDungeonsList = len(dungeonsList)
    for i in range (lenDungeonsList) :
        tmp = k
        cnt = 0
        for j in range (len(dungeonsList[i])) :
            if dungeonsList[i][j][0] <= tmp :
                cnt += 1
                tmp -= dungeonsList[i][j][1]
        if (maxCnt <= cnt) :
            maxCnt = cnt
              
    return maxCnt