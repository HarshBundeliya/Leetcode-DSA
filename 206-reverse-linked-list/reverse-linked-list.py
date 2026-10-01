# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity = O(n)
# Space Complexity = O(1) 
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        previous  = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous