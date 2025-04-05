# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        curr = head 
        bin_val = '0b'
        while curr:
            bin_val += str(curr.val)
            curr = curr.next  

        val = int(bin_val, 2)     
        print(val)
        return val