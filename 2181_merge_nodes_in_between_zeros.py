# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = head.next
        start = head
        while start:
            end = start
            sum = 0
            while end.val != 0:
                sum += end.val
                end = end.next
            start.val = sum
            start.next = end.next
            start = start.next
        return head