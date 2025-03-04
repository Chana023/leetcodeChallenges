# https://leetcode.com/problems/single-number/description/

from collections import Counter

class Solution():
    def singleNumber(self, nums):
        count = Counter(nums)
        
        for key, value in  count.items():
            if value == 1:
                print (key)
                return key

sols = Solution()
sols.singleNumber([4,1,2,1,2])