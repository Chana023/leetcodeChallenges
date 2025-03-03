# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        if not nums:
            return None

        mid_node = len(nums) // 2
        return TreeNode(nums[mid_node],self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1:]))