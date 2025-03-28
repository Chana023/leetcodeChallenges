# https://leetcode.com/problems/sqrtx/description/

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            m = l + (r-l) // 2
            square = m * m
            if square == x:
                return m
            elif square < x:
                l = m + 1
            else:
                r = m - 1
        return r

sol = Solution()
sol.mySqrt(8)