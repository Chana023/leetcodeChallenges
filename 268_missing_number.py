# https://leetcode.com/problems/missing-number/description/

class Solution():
    def missingNumber(self, nums):
        len_nums = len(nums) + 1
        correct_nums = [ x for x in range(0, len_nums, 1)]

        for value in correct_nums:
            if value not in nums:
                print(value)
                return value


sol = Solution()
sol.missingNumber([9,6,4,2,3,5,7,0,1])