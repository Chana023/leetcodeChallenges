# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/description/

def minimumSum(nums):

    if len(nums) < 3:
        return -1
    
    min_sum = float('inf')

    for i in range(1, len(nums) - 1):
        left_min = min(nums[:i])
        right_min = min(nums[i+1:])

        if nums[i] > left_min and nums[i] > right_min:
            min_sum = min(min_sum, left_min + nums[i] + right_min)

    return min_sum if min_sum != float('inf') else -1 



minimumSum([5,4,8,7,10,2])