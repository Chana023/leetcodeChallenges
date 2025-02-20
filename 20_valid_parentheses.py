# https://leetcode.com/problems/valid-parentheses/description/

class Solution():
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict_brack = {
            ')': '(', 
            ']': '[', 
            '}': '{'
        }

        for char in s:
            if char in dict_brack:
                if stack and stack[-1] == dict_brack[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack


sols = Solution()
print(sols.isValid("([])"))