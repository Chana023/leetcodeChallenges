# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    for i in range(0, len(nums), 1):
        for j in range(i + 1, len(nums), 1):
            if nums[i] + nums[j] == target:
                return (i, j)

twoSum([3,3], 6)

# Above is brute force , better implementation is to use another algo

def twoSumBetter(nums, target):
    pair = {}

    for i, num in enumerate(nums):
        if target - num in pair:
            print ([i, pair[target-num]])
            return [i, pair[target-num]]
        pair[num] = i


twoSumBetter([2,7,11,15], 9)