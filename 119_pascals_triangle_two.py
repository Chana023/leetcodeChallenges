# https://leetcode.com/problems/pascals-triangle-ii/

class Solution():
    def getRow(self, rowIndex):
        if rowIndex == 0:
            print([1])
            return [1]
        
        if rowIndex == 1:
            print([1,1])
            return[1,1]

        result = [[1], [1,1]]
        row =  2
        
        while row <= rowIndex:
            new_row = [1]
            old_row = result[-1]

            for i in range(1, len(old_row)):
                new_row.append(old_row[i - 1] + old_row[i])

            new_row.append(1)
            result.append(new_row)

            row += 1

        print(new_row)
        return result

sols = Solution()
sols.getRow(1)