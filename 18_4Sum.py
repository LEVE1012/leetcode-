#Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

#0 <= a, b, c, d < n
#a, b, c, and d are distinct.
#nums[a] + nums[b] + nums[c] + nums[d] == target

#You may return the answer in any order.

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

#这道题的思路和之前的差不多，都是运用了双指针，只不过这次是双重遍历
#时间复杂度为O(n^3)，空间复杂度为O(n^3)（主要是输出结果的复杂度）
