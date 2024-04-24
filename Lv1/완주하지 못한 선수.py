def solution(participant, completion):
    lenP = len(participant)
    lenC = len(completion)
    
#     방법 1
#     for i in range (lenP) :
#         isComplete = False
#         for j in range (len(completion)) :
#             if participant[i] == completion[j] :
#                 isComplete = True
#                 del completion[j]
#                 break
#         if isComplete == False :
#             return participant[i]
       
    # 방법 2
    dic = {}
    
    for i in range (lenP) :
        dic[participant[i]] = 0
    for i in range (lenP) :
        dic[participant[i]] += 1
    
    for i in range(lenC) :
        dic[completion[i]] -= 1
        
    for i in range(lenP) :
        if dic[participant[i]] != 0 :
            return participant[i]