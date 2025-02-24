# https://leetcode.com/problems/search-insert-position/description/

class Solution():
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            print(nums.index(target))
            return nums.index(target)
            
        elif target > nums[len(nums)-1]:
            print(nums.index(nums[len(nums)-1]) + 1)
            return nums.index(nums[len(nums)-1]) + 1
        else:
            curr_val = float('inf')
            for value in nums:
                if value > target:
                    print(nums.index(value))
                    return nums.index(value)
                    break

sols = Solution()
sols.searchInsert([1,3,5,6], 2)