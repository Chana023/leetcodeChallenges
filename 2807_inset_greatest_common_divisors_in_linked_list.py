# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

class Solution():
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr and curr.next:
            gcd_value = gcd(curr.val, curr.next.val)
            gcd_node = ListNode(gcd_value)
            gcd_node.next = curr.next
            curr.next = gcd_node

            curr = gcd_node.next
            
        return head