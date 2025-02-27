# https://leetcode.com/problems/add-binary/description/

class Solution():
    def addBinary(self, a, b):
        a = int(a, 2)
        b = int(b, 2)

        result = a + b
        print(result)

        print(bin(result)[2:])
        return bin(result)[2:]


sols = Solution()
sols.addBinary("11", "1")