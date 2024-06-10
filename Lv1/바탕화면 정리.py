def solution(wallpaper):
    answer = []
    
    lux = len(wallpaper)
    luy = len(wallpaper[0])
    rdx = 0
    rdy = 0
    for i in range (len(wallpaper)) :
        for j in range(len(wallpaper[i])) :
            if wallpaper[i][j] == "#" :
                if i < lux :
                    lux = i
                if j < luy : 
                    luy = j
                if i > rdx - 1 :
                    rdx = i + 1
                if j > rdy - 1 :
                    rdy = j + 1
    
    return [lux, luy, rdx, rdy]
