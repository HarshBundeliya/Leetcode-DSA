# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        current = head
        len_list = 0
        while current:
            current = current.next
            len_list += 1 
        
        target = len_list - n
        if target == 0:
            return head.next

        new_current = head
        for i in range(target - 1):
            new_current = new_current.next
        
        if new_current and new_current.next:
            new_current.next = new_current.next.next
        
        return head