# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        slow = head
        fast = head
        while n>=0:
            if fast:
                fast = fast.next
                n-=1
            else:
                return head.next
                
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head