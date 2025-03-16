# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

from collections import Counter

class Solution():
    def intersect(self, nums1, nums2):
        sortednums1 = sorted(nums1)
        sortednums2 = sorted(nums2)

        i = 0
        j = 0
        output = []

        while i < len(sortednums1) and j < len(sortednums2):
            if sortednums1[i] < sortednums2[j]:
                i += 1
            elif sortednums2[j] < sortednums1[i]:
                j += 1
            else:
                output.append(sortednums1[i])
                i += 1
                j += 1

        print(output)
        return output



sol = Solution()
sol.intersect([1,2,2,1],[2,2])