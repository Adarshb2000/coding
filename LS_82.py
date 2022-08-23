#  Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode):
        start = ListNode(val=101, next=head)
        itr = start
        while itr is not None and itr.next is not None:
            while itr:
                temp = itr.next
                val = temp.val
                i = -1
                while temp and val == temp.val:
                    temp = temp.next
                    i += 1
                
                if i:
                    itr.next = temp
                else:
                    break
            itr = itr.next
        
        return start.next
        