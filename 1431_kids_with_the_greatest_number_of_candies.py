# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_cand = max(candies)

        res = []
        for value in candies:
            if value + extraCandies >= max_cand:
                res.append(True)
            else:
                res.append(False)

        print(res)
        return res

sol = Solution()
sol.kidsWithCandies([2,3,5,1,3], 3)