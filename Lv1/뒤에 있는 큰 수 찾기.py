# 방법 1 - 시간 초과
# def solution(numbers):
#     lenNumbers = len(numbers)
#     answer = [-1] * lenNumbers
    
#     for i in range (lenNumbers) :
#         for j in range (i + 1, lenNumbers) :
#             if numbers[i] < numbers[j] :
#                 answer[i] = numbers[j]
#                 break

#     return answer


# 방법 2 - 시간 초과
# def solution(numbers):
#     max = 100000000
#     lenNumbers = len(numbers)
#     answer = [-1] * lenNumbers
    
#     for i in range (lenNumbers) :
#         if max <= numbers[i] :
#             continue
#         flag = 1
#         for j in range (i + 1, lenNumbers) :
#             if numbers[i] < numbers[j] :
#                 answer[i] = numbers[j]
#                 flag = 0
#                 break
#         if flag == 1 :
#             max = numbers[i]

#     return answer

# 방법 3
def solution(numbers) :
    stack = []
    lenNumbers = len(numbers)
    answer = [-1] * lenNumbers

    for i in range(lenNumbers) :
        while stack and (numbers[stack[-1]] < numbers[i]) :
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer