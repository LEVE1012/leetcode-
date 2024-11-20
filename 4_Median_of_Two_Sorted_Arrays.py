#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        while left <= right:
            i = (left + right) // 2
            j = half_len - i

            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if (m + n) % 2 == 0:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
                else:
                    return max(nums1_left_max, nums2_left_max)
            elif nums1_left_max > nums2_right_min:
                right = i - 1 #i左移
            else:
                left = i + 1 #i右移
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
#这是我们遇到的第一个difficult题目，而这个题目也用到了一个新算法：二分查找
#首先挑选较短的数组进行优先查找，始终满足i + j = half_len，然后通过二分法进行查找 i 最终适合的位置
#那么 i 究竟需要在什么样的位置上呢？这就需要一个条件判断，nums1左侧最大值小于nums2右侧最小值，nums2左侧最大值小于nums1右侧最小值
#当我们真正找到满足这一条件的位置的时候，除nums1，nums2左侧最大值以外，左侧全部为有序排列，右侧也是同理
#这个时候，我们无需在意左侧和右侧究竟是如何有序排列的，只需要关注这四个数的排列顺序
#如果合并数组的数量为偶数，则需要将中间两个数加起来除以二，奇数则直接将左侧的最大值输出即可
#如果不满足某个条件，那我们就需要想 i 到底是偏左还是偏右，如果 i 偏右，那么从 i 到右侧的全部都可以排除，反之左侧亦然
#有点像初中学的牛顿二分法求一个函数的近似解，当然最有意思的还是这个中间值的寻找过程，跳过没用的前后范围，可以大大减少工作量
#时间复杂度为O(log(min(m, n))，空间复杂度为O(1)
