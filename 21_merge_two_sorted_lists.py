# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        req = []
        cur=list1
        while cur!=None:
            req.append(cur.val)
            cur=cur.next
        cur=list2
        while cur!=None:
            req.append(cur.val)
            cur=cur.next
        cur=list1
        while cur.next!=None:
            cur=cur.next
        cur.next=list2
        req=sorted(req)
        cur=list1
        for i in req:
            cur.val=i
            cur=cur.next
        return list1
        