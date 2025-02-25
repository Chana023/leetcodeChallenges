# https://leetcode.com/problems/length-of-last-word/description/

class Solution():
    def lengthOfLastWord(self, s):
        s = s.rstrip()

        list_s = s.split(' ')
        len_s = len(list_s)
        last_word = list_s[len_s-1]
        print(len(last_word))
        return len(last_word)

sols = Solution()
sols.lengthOfLastWord('   fly me   to   the moon  ')