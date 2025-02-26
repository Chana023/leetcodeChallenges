# https://leetcode.com/problems/plus-one/description/

class Solution():
    def plusOne(self, digits):
        number = int(''.join(map(str, digits)))
        number = number + 1

        result = [int(x) for x in str(number)]
        print(result)
        return result

sols = Solution()
sols.plusOne([1,2,3])