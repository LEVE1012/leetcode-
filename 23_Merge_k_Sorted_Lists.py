#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

#Merge all the linked-lists into one sorted linked-list and return it.

import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(-1)
        current = dummy

        heap = []

        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))

        while heap:
            val, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))

        return dummy.next
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

#这道题主要使用了一个最小堆的数据结构，以此来保障每次取出的值都是非空子链表中首节点的最小值，
#需要注意的点有heapq的语法，l的非空判定（否则会无限循环）
#也可以用分治法来解决，用对数的形式来化简数组
#时间复杂度为O(Nlogk)（N为节点总数，k为子链表的个数），空间复杂度为O(1)

#分治法
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        return self.merge_divide_and_conquer(lists, 0, len(lists) - 1)

    def merge_divide_and_conquer(self, lists, left, right):
        if left == right:  # Base case: only one list to merge
            return lists[left]
        
        mid = (left + right) // 2
        
        # Recursively divide and merge the left and right halves
        left_half = self.merge_divide_and_conquer(lists, left, mid)
        right_half = self.merge_divide_and_conquer(lists, mid + 1, right)
        
        # Merge the two halves
        return self.merge_two_lists(left_half, right_half)
    
    def merge_two_lists(self, l1, l2):
        # Merge two sorted linked lists
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # If any of the lists is not exhausted, attach the remaining part
        current.next = l1 if l1 else l2
        
        return dummy.next

  #时间复杂度相同，空间复杂度为O(logk)（由于采用了递归栈，所以logk即为递归的最大深度）
