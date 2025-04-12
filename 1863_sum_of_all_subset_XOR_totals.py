# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for num in nums:
            total |= num
        return total * (1 << (len(nums) - 1))