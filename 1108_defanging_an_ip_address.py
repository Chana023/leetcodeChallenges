# https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        
        res = address.replace(".", "[.]")
        print(res)
        return res

sol = Solution()
sol.defangIPaddr("1.1.1.1")