# https://leetcode.com/problems/range-sum-query-immutable/description/

class NumArray():

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        sum = 0
        for i in range(left, right + 1):
            sum = sum + self.nums[i]

        return sum


sol = NumArray([-2,0,3,-5,2,-1])
result_1 = sol.sumRange(0,2)
result_2 = sol.sumRange(2,5)
result_3 = sol.sumRange(0, 5)

print(result_1, result_2, result_3)

