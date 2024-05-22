def solution(dots):
    # 0, 1 과 2, 3
    if (dots[0][0] - dots[1][0]) / (dots[0][1] - dots[1][1]) == (dots[2][0] - dots[3][0]) / (dots[2][1] - dots[3][1]) :
        return 1
    if (dots[0][0] - dots[1][0]) / (dots[0][1] - dots[1][1]) == (dots[3][0] - dots[2][0]) / (dots[3][1] - dots[2][1]) :
        return 1
    
    # 0, 2 와 1, 3
    if (dots[0][0] - dots[2][0]) / (dots[0][1] - dots[2][1]) == (dots[1][0] - dots[3][0]) / (dots[1][1] - dots[3][1]) :
        return 1
    if (dots[0][0] - dots[1][0]) / (dots[0][1] - dots[1][1]) == (dots[3][0] - dots[1][0]) / (dots[3][1] - dots[1][1]) :
        return 1
    
    # 0, 3 과 1, 2
    if (dots[0][0] - dots[3][0]) / (dots[0][1] - dots[3][1]) == (dots[1][0] - dots[2][0]) / (dots[1][1] - dots[2][1]) :
        return 1
    if (dots[0][0] - dots[3][0]) / (dots[0][1] - dots[3][1]) == (dots[2][0] - dots[1][0]) / (dots[2][1] - dots[1][1]) :
        return 1

    return 0