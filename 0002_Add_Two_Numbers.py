#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 

#and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()
        current, carry = dummy_head, 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, total = divmod(val1 + val2 + carry, 10)

            current.next = ListNode(total)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next
        
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
      
#这段程序采用了类似于计算机组成原理中的加法器的方式，一步一步向上进位，最后输出结果。
#需要注意的是，dummy_head只是一个形式头节点，它的next节点才是最后的返回值
#时间复杂度为O(max(m, n)，空间复杂度为O(1）
