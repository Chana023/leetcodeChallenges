# https://leetcode.com/problems/remove-element/description/

class Solution():
    def removeElement(self, nums, val):
        for i in range(nums.count(val)):
            nums.remove(val)
        return(len(nums))



sols = Solution()
sols.removeElement([3,2,2,3], 3)