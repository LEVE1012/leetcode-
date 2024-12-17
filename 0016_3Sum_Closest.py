#Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

#Return the sum of the three integers.

#You may assume that each input would have exactly one solution.

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = float('-inf')

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total

                if abs(total - target) < abs(target - closest_sum):
                    closest_sum = total
                
                if total < target:
                    left += 1
                else:
                    right -= 1


        return closest_sum
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

#事实上这个方法是效率不错的一个方法，在做上一道题的时候，我们可以联想到第一道题哈希表边存储边查找的方法，
#上一道题可以用哈希表查找，当确定了一个数的时候，剩下的数便可以转换为两数之和问题，但是这一道题用哈希表和双指针差不了多少，甚至双指针可能更快
