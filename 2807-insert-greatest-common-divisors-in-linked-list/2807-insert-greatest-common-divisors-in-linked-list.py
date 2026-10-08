class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        curr = head

        while curr and curr.next:
            nxt = curr.next

            gcd_val = gcd(curr.val, nxt.val)

            newNode = ListNode(gcd_val)

            curr.next = newNode
            newNode.next = nxt

            curr = nxt

        return head