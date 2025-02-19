# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    
sols = Solution()
sols.removeDuplicates([1,1,2])