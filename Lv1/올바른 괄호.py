def solution(s):
    stack = []
    lenS = len(s)
    
    for i in range (lenS) :
        if (s[i] == '(') :
            stack.append(s[i])
        if (s[i] == ')') :
            if len(stack) == 0 :
                return False
            stack.pop()
            
    if len(stack) != 0 :
        return False
    return True