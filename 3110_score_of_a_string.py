# https://leetcode.com/problems/score-of-a-string/description/

class Solution():
    def scoreOfString(self, s):
        sum = 0 

        for i in range(1, len(s)):
            sum = sum + abs(ord(s[i]) - ord(s[i - 1]))

        print(sum) 
        return sum

sol = Solution()
sol.scoreOfString("zaz")