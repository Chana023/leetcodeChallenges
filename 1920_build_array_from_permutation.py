# https://leetcode.com/problems/build-array-from-permutation/description/

class Solution():
    def buildArray(self, nums):
        result = []
        for i in range(0, len(nums)):
            result.append(nums[nums[i]])

        print(result)
        return result

sols = Solution()
sols.buildArray([0, 2, 1, 5, 3, 4])