# https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution():
    def intersection(self, nums1, nums2):
        result =  set(nums1) & set(nums2)
        result = list(result)

        print(result)
        return result

sol = Solution()
sol.intersection([4,9,5], [9,4,9,8,4])