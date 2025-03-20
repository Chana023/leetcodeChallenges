# https://leetcode.com/problems/max-consecutive-ones/description/

class Solution():
    def findMaxConsecutiveOnes(self, nums):
        curr_count = 0
        curr_max = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count = curr_count + 1
            else:
                curr_count = 0

            if curr_count > curr_max:
                curr_max = curr_count

            print(i, curr_max)
        return curr_max


sol = Solution()
sol.findMaxConsecutiveOnes([1,0,1,1,0,1])