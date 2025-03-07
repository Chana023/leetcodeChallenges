# https://leetcode.com/problems/majority-element/description/

from collections import Counter

class Solution():
    def majorityElement(self, nums):
        maj_elem = len(nums) // 2

        count_nums = Counter(nums)
        count_nums_sorted = list (sorted(count_nums.items(), key=lambda item: item[1], reverse=True))
        
        print(count_nums_sorted[0][0])
        return count_nums_sorted[0][0]


sols = Solution()
sols.majorityElement([3,2,3])