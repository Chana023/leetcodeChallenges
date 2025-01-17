
def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    running_sum = []
    sum = 0
    for i in nums:
        sum = sum + i
        running_sum.append(sum)

    return running_sum
    
print(runningSum([1,2,3,4]))

