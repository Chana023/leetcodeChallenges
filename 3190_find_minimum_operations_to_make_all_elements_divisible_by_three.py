# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/

class Solution():
    def minimumOperations(self, nums):
        op = 0
        for i in nums:
            if i % 3:
                op += 1
        return op

sol = Solution()
sol.minimumOperations([1,2,3,4])