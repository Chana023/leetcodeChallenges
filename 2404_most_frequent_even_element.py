# https://leetcode.com/problems/most-frequent-even-element/

from collections import Counter, OrderedDict

def mostFrequentEven(nums):
    counter_nums = Counter(nums)
    counter_nums = OrderedDict(sorted(counter_nums.items(),reverse=True))

    print(counter_nums)
    delete_keys = []
    for key, value in counter_nums.items():
        if key % 2 != 0 and key in counter_nums:
            delete_keys.append(key)

    for value in delete_keys:
        if value in counter_nums:
            del counter_nums[value]

    max = 0
    output = -1
    for num, count in counter_nums.items():
        if count > max:
            max, output = count, num
        elif count == max:
            output = min(num,output)
    return output

def betterMostFrequentEven(nums):
    even_map = {}
    for value in nums:
        if value % 2 == 1:
            even_map[value] = even_map.get(value,0) + 1

        if not even_map:
            return -1
        
    max_value = max(even_map.values())

    return min(x for x in even_map if even_map[x] == max_value)


print(mostFrequentEven([0,1,2,2,4,4,1]))