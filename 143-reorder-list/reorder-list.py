# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.

        Time Complexity = O(n)
        Space Complexity = O(1)

        Remember these three core steps: Find Middle → Reverse Second Half → Merge Alternately
        """
        # Step 1: Find the middle of the linked list
        slow = head 
        fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # Step 2: Split the list into two halves
        second_half = slow.next
        slow.next = None

        # Step 3: Reverse the second half
        def reverse_list(current):
            previous = None
            while current:
                next_node = current.next
                current.next = previous
                previous = current 
                current =  next_node
            return previous

        second_half = reverse_list(second_half)

        # Step 4: Merge both halves alternately
        first = head
        second = second_half
        while second:
            new_first = first.next
            new_second = second.next

            first.next = second
            second.next = new_first

            first = new_first
            second = new_second