#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

#Find two lines that together with the x-axis form a container, such that the container contains the most water.

#Return the maximum amount of water a container can store.

#Notice that you may not slant the container.

class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            h = min(height[right], height[left])
            max_water = max(width * h, max_water)

            if height[left] < height[right]:
                left += 1
            else:   
                right -= 1
            
        return max_water
        """
        :type height: List[int]
        :rtype: int
        """

#这道题采用的方法是贪心算法，通过left和right分别从两边开始收缩的原理，进而逐步确定水杯容量的最大值，
#对于算法正确性的总结实际上可以通过反证法，假设当前缩短的是较长的那边，那么缩短之后新的水杯容量只会小于或等于原先的容量，因此可以通过贪心算法获取局部最优解
#最终的时间复杂度为O(n)，空间复杂度为O(1)
