# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

from collections import Counter

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed = set(allowed)
        count = 0
        
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        
        return len(words) - count


        

sol = Solution()
sol.countConsistentStrings('ab', ["ad","bd","aaab","baa","badab"])