# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        curr1 = list1
        curr2 = list2

        if curr1.val <= curr2.val:
            new_head = curr1
            curr1 = curr1.next
        else:
            new_head = curr2
            curr2 = curr2.next

        temp = new_head

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                temp.next = curr1
                curr1 = curr1.next
                temp = temp.next
            else:
                temp.next = curr2
                curr2 = curr2.next
                temp = temp.next
        
        if curr1:
            temp.next = curr1
        elif curr2:
            temp.next = curr2
        
        return new_head



# two sorted lists
# first element of new list will be first element of either sorted list
# 1 
# curr1 = 2, curr2 = 1