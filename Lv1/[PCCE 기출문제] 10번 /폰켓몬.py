def solution(nums):
    answer = 0
    N = len(nums)
    
    nums.sort(reverse=False)
    print(nums)
    
    Pocketmon = 0
    numPkm = 0
    for i in range(N) :
        if (Pocketmon != nums[i]) :
            answer += 1
            Pocketmon = nums[i]
            numPkm += 1
            if (numPkm == N // 2) :
                break
    
    return answer