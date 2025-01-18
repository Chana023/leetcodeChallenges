# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def middleNode(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow






    
        