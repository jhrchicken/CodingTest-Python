def solution(numbers, k):
    answer = 0
    
    len_numbers = len(numbers)
    for i in range (k - 1) :
        answer = (answer + 2) % len_numbers

    return answer + 1