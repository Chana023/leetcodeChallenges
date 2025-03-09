# https://leetcode.com/problems/contains-duplicate/description/

from collections import Counter

class Solution():
    def containsDuplicate(self, nums):
        count_nums = Counter(nums)

        for key, value in count_nums.items():
            if value > 1:
                print('true')
                return True
        
        print(False)
        return False

sols = Solution()
sols.containsDuplicate([1,1,1,3,3,4,3,2,4,2])

