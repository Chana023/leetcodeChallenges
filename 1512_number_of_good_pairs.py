# https://leetcode.com/problems/number-of-good-pairs/description/

class Solution():
    def numIdenticalPairs(self, nums):
        count = 0
        for value in nums:
            count -= 0.5
            for value2 in nums:
                if value == value2:
                    count += 0.5

        count = int(count)
        print(count)
        return count

sol = Solution()
sol.numIdenticalPairs([1,2,3])