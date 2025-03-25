# https://leetcode.com/problems/array-partition/description/

class Solution():
    def arrayPairSum(self, nums):
        nums = sorted(nums)

        res = 0
        for i in range(0, len(nums), 2):
            res +=  nums[i]

        print(res)
        return res

sol = Solution()
sol.arrayPairSum([1,4,3,2])