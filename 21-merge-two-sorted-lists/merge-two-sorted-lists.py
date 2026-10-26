# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        """
        Time Complexity = O(m+n); where m=len(list1) and n = len(list2)
        Space Complexity = O(1)
        """
        dummy = ListNode(0)
        current = dummy 
        while list1 and list2:
            if list1.val >= list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next

        current.next = list2 if list2 else list1
        
        return dummy.next