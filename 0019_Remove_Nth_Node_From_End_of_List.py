#Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        node_pointer1 = dummy
        node_pointer2 = head
        res = []
        for _ in range(n):
            node_pointer2 = node_pointer2.next
        
        while node_pointer2:
            node_pointer1 = node_pointer1.next
            node_pointer2 = node_pointer2.next
        
        node_pointer1.next = node_pointer1.next.next

        return dummy.next
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

#和之前做的第二题比较像，通过双指针的方式（快慢指针结合），来达到“删除节点”的效果
#这里有一个需要注意的点就是这个形式头节点dummy，如果是要删除原本链表的头节点的话，常规方法会有局限性，所以通过创建一个新的形式头节点来进行操作
