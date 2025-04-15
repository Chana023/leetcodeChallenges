# https://leetcode.com/problems/convert-date-to-binary/description/

class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        vals = date.split('-')

        res = ""
        for val in vals:
            bval = bin(int(val))
            # print()
            res += bval[2:] + '-' 
        
        res = str(res[:-1])
        print(res)
        return res

sol = Solution()
sol.convertDateToBinary("1900-01-01")