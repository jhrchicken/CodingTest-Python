def solution(board):
    n = len(board)
    
    warning = [[0 for j in range(n + 2)] for i in range(n + 2)]
    
    
    for i in range (n) :
        for j in range (n) :
            if board[i][j] == 1 :
                warning[i][j] = 1
                warning[i][j + 1] = 1
                warning[i][j + 2] = 1
                warning[i + 1][j] = 1
                warning[i + 1][j + 1] = 1
                warning[i + 1][j + 2] = 1
                warning[i + 2][j] = 1 
                warning[i + 2][j + 1] = 1
                warning[i + 2][j + 2] = 1
    
    cnt = 0
    for i in range (1, n + 1) :
        for j in range (1, n + 1) :
            if warning[i][j] == 1 :
                cnt += 1
    
    return (n * n) - cnt