def solution(park, routes):
    route = []
    lenParkH = len(park)
    lenParkW = len(park[0])
    lenRoutes = len(routes)
    
    H = 0
    W = 0
    for i in range (lenParkH) :
        for j in range (lenParkW) :
            if park[i][j] == "S" :
                H = i
                W = j
                break
                
    for i in range (lenRoutes) :
        route = routes[i].split()
        if route[0] == 'N' :
            if H - int(route[1]) < 0 :
                continue
            for j in range (H - int(route[1]), H) :
                isHuddle = 0
                if park[j][W] == "X" :
                    isHuddle = 1
                    break
            if isHuddle == 1 :
                continue
            H -= int(route[1])
        if route[0] == 'S' :
            if H + int(route[1]) > lenParkH - 1 :
                continue
            for j in range (H, H + int(route[1]) + 1) :
                isHuddle = 0
                if park[j][W] == "X" :
                    isHuddle = 1
                    break
            if isHuddle == 1 :
                continue
            H += int(route[1])
        if route[0] == 'W' :
            if W - int(route[1]) < 0 :
                continue
            for j in range (W - int(route[1]), W) :
                isHuddle = 0
                if park[H][j] == "X" :
                    isHuddle = 1
                    break
            if isHuddle == 1 :
                continue
            W -= int(route[1])
        if route[0] == 'E' :
            if W + int(route[1]) > lenParkW - 1 :
                continue
            for j in range (W, W + int(route[1]) + 1) :
                isHuddle = 0
                if park[H][j] == "X" :
                    isHuddle = 1
                    break
            if isHuddle == 1 :
                continue
            W += int(route[1])
    
    return [H, W]