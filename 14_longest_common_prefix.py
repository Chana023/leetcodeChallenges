# https://leetcode.com/problems/longest-common-prefix/description/

class Solution():
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix) and prefix:
                prefix = prefix[:-1]
            if not prefix:
                return ""
        
        print(prefix)
        return prefix


sols = Solution()
sols.longestCommonPrefix(["flower","flow","flight"])