# https://leetcode.com/problems/set-mismatch/description/\

from collections import Counter

def findErrorNums(nums):
    counter = Counter(nums)
    result = []

    correct_nums = [x for x in range(1, len(nums)+1, 1)]

    counter_correct_nums = Counter(correct_nums)

    print(counter_correct_nums)

    for key, val in counter.items():
        if val == 2:
            result.append(key)

    for key, val in counter_correct_nums.items():
        if key not in counter:
            result.append(key)

    print(result)
    return result

findErrorNums([3,2,2])