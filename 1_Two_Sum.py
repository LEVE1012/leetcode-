#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {}
        for i, num in enumerate(nums):
            targetNum = target - num
            if targetNum in num_to_index:
                return [num_to_index[targetNum], i]
            num_to_index[num] = i

#这道题采用了哈希表的方式，在遍历的过程中顺便构建哈希表，最后将查找出的结果打印出来，时间复杂度为O(n)，空间复杂度为O(n)
