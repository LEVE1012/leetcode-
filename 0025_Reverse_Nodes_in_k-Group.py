# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def reverse_linked_list(head, k):
            prev = None
            current = head
            while k > 0:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                k -= 1
            return prev, head
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        group_prev = dummy

        while True:
            group_end = group_prev
            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    return dummy.next
        
            group_next = group_end.next
            group_end = None

            group_start = group_prev.next
            new_group_start, new_group_end = reverse_linked_list(group_start, k)

            group_prev.next = new_group_start
            group_start.next = group_next
            
            group_prev = new_group_end
        
        return dummy.next

#这里值得注意的是倒转链表顺序的函数，其中next和指针交错纵横会导致一时半会理解不了的情况，理解即可
