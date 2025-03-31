# https://leetcode.com/problems/shuffle-the-array/description/

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []

        for i in range(0, len(nums)//2):
            res.append(nums[i])
            res.append(nums[i + n])

        print(res)
        return res


sol = Solution()
sol.shuffle([2,5,1,3,4,7], 3)