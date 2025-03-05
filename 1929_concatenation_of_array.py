# https://leetcode.com/problems/concatenation-of-array/

class Solution():
    def getConcatenation(self, nums):
        ans = nums + nums
        print(ans)
        return ans

sols = Solution()
sols.getConcatenation([1,2,1])