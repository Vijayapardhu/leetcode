

class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left == right:
            return head

        # Use a dummy node to handle cases where the head is reversed
        dummy = ListNode(0, head)
        prev = dummy

        # Reach the node just before the start of the reversal
        for _ in range(left - 1):
            prev = prev.next

        # curr is the node that will be moved, next_node is the node to be moved next
        curr = prev.next
        
        # Perform in-place reversal using pointer manipulation
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next