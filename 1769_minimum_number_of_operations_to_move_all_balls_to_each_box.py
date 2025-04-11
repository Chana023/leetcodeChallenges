# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution(object):
    def minOperations(self, boxes):
        
        ball_loc = []

        for i in range(len(boxes)):
            if boxes[i] == '1':
                ball_loc.append(i)

        res = []
        for i in range(len(boxes)):
            opers = 0
            for j in ball_loc:
                opers = opers + abs(i - j)
            res.append(opers)

        print(res)
        return res
            

sol = Solution()
sol.minOperations("001011")