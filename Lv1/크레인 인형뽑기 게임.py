def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)
    
    for i in range (len(moves)) :
        for j in range (N) :
            if board[j][moves[i] - 1] != 0 :
                stack.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break
        if len(stack) >= 2 :
            if (stack[-1] == stack[-2]) :
                answer += 2
                stack.pop()
                stack.pop()

    return answer