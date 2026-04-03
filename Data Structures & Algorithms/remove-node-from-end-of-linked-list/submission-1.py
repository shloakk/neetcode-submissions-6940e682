# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        temp = head
        for i in range(n):
            temp = temp.next
        
        if not temp:
            return curr.next

        while temp.next:
            curr = curr.next
            temp = temp.next
        
        curr.next = curr.next.next
        
        return head
