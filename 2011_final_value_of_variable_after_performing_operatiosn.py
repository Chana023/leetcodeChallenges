# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution():
    def finalValueOperations(self, operations):
        x = 0
        for op in operations:
            if op == 'X++' or op == '++X':
                x = x + 1
            elif op == 'X--' or op == '--X':
                x = x - 1

        print(x)
        return(x)


sol = Solution()
sol.finalValueOperations(["X++","++X","--X","X--"])