#Given an array of intervals intervals where intervals[i] = [starti, endi], 

#return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

#Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x: x[1])

        non_overlapping_count = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start >= prev_end:
                non_overlapping_count += 1
                prev_end = end
        return len(intervals) - non_overlapping_count
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

#使用的是贪心算法，通过将结束时间排序的方法，找到每一步的最优解，即最早结束时间，以此为依据找出尽可能多需要保留的节点，最后两者做差，计算出需要删除的最小节点数量
#时间复杂度为O(nlog(n))（排序占主要事件消耗），空间复杂度取决于排序算法需要的空间，最优为原地排序O(1)，最差为需要辅助空间的情况，为O(n)
