# https://leetcode.com/problems/transform-array-by-parity/description/

class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            elif nums[i] % 2 != 0:
                nums[i] = 1

        nums.sort()

        print(nums)
        return nums

sol = Solution()
sol.transformArray([1,5,1,4,2])    
