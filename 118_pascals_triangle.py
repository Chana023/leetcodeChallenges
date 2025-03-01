# https://leetcode.com/problems/pascals-triangle/description/

class Solution():
    def generate(self, numRows):


        if numRows == 1:
            return [[1]]
        
        first_list = [1]
        second_list = [1, 1]

        result = [first_list, second_list]
        row =  3
        
        while row <= numRows:
            new_row = [1]
            old_row = result[-1]

            for i in range(1, len(old_row)):
                new_row.append(old_row[i - 1] + old_row[i])

            new_row.append(1)
            result.append(new_row)

            row += 1

        print(result)
        return result






sols = Solution()
sols.generate(5)