# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/

from collections import Counter

class Solution():
    def getSneakyNumbers(self, nums):
        
        count_nums = Counter(nums)
        res = []

        for key, val in count_nums.items():
            if val == 2:
                res.append(key)

        print(res)
        return res

sol = Solution()
sol.getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2])