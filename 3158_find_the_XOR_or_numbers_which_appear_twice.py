# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

from collections import Counter

def duplicateNumbersXOR(nums):
    count_nums = Counter(nums)
    nums_plus_1 = []
    
    for key, value in count_nums.items():
        if value > 1:
            nums_plus_1.append(key)


    if nums_plus_1: 
        result = nums_plus_1[0] 
    else:
        result = 0
    for i in range(1, len(nums_plus_1)):
        result = result ^ nums_plus_1[i]

    print(result)
    return result



duplicateNumbersXOR([1,2,2,1])