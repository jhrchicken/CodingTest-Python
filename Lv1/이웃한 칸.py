def solution(board, h, w):
    answer = 0
    n = len(board)
    
    if h > 0 and board[h][w] == board[h - 1][w] :
        answer += 1
    if h < n - 1 and board[h][w] == board[h + 1][w] :
        answer += 1
    if w > 0 and board[h][w] == board[h][w - 1] :
        answer += 1
    if w < n - 1 and board[h][w] == board[h][w + 1] :
        answer += 1
    
    return answer