# https://leetcode.com/problems/intersection-of-multiple-arrays/

from collections import Counter, defaultdict

def intersection(nums):
    combined_list = []
    results = []

    if len(nums) == 1:
        for value in nums:
            value.sort()
            return value

    for value in nums:
        combined_list = combined_list + value

    count_dict = Counter(combined_list)
    max_count_val = max(count_dict.values())

    result = [key for key,value in count_dict.items() if value == max_count_val and max_count_val > 1 ]

    result.sort()
    return result

def betterIntersection(nums):
    res = set(nums[0])
    for i in range(1, len(nums)):
        res &= set(nums[i])
        res = list(res)
        res.sort()
        return res
    

print(intersection([[44,21,48]]))