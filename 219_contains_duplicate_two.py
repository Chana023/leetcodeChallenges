# https://leetcode.com/problems/contains-duplicate-ii/description/
from collections import Counter

class Solution():
    def containsNearbyDuplicates(self, nums, k):
        d_holder = {}

        for i, value in enumerate(nums):
            if value in d_holder and abs(i - d_holder[value]) <= k:
                return True
            else:
                d_holder[value] = i

        return False

        
        

sols = Solution()
sols.containsNearbyDuplicates([1,2,3,1], 3)