# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution():
    def findDisappearredNumbers(self, nums):
        max_num = len(nums) 
        correct_list = [x for x in range(1,max_num + 1 )]
        correct_set = set(correct_list)

        nums.sort()
        nums_set = set(nums)

        res = correct_set - nums_set

        print(res)
        return list(res)



sol = Solution()
sol.findDisappearredNumbers([4,3,2,7,8,2,3,1])