# https://leetcode.com/problems/jewels-and-stones/description/

from collections import Counter

class Solution():
    def numJewelsInStones(self, jewels, stones):
        count_stones = Counter(stones)
        print(count_stones)

        count = 0
        for val in jewels:
            if val in count_stones.keys():
                count = count + count_stones[val]

        print(count)
        return count

sol = Solution()
sol.numJewelsInStones("aA", "aAAbbbb")