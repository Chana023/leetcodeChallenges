# https://leetcode.com/problems/find-words-containing-character/description/

class Solution():
    def findWordsContaining(self, words, x):

        res = []        
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)

        print(res)
        return res

sol = Solution()
sol.findWordsContaining(["leet","code"], 'e')