# https://leetcode.com/problems/move-zeroes/description/
from collections import Counter

class Solution():
    def moveZeroes(self, nums):
        
        num_zeros = 0
        count_nums = Counter(nums)

        num_of_zeroes = count_nums[0]

        for i in range(0, num_of_zeroes):
            index = nums.index(0)
            print(index)
            nums.pop(index)
            nums.append(0)

        print(nums)
        return nums
        

sol = Solution()
sol.moveZeroes([0,1,0,3,12])