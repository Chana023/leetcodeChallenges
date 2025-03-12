# https://leetcode.com/problems/summary-ranges/description/

class Solution():
    def summaryRanges(self, nums):
        output = []
        idx = 0
        while idx < len(nums):
            beg = nums[idx]
            while idx+1 < len(nums) and nums[idx+1] == nums[idx] + 1:
                idx += 1
            last = nums[idx]
            if beg == last:
                output.append(str(last))
            else:
                output.append(str(beg) + "->" + str(last))
            idx += 1
        print(output)
        return output


sols = Solution()
sols.summaryRanges([0,1,2,4,5,7])