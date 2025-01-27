class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = reversed(nums[i + 1:])
#求取下一个对应的整型排列，这里有一个需要注意的点那就是在遍历j的过程中，由于nums[i]必然不是最大的数，因此表中存在一个数nums[j] > nums[i]，所以不需要确认j > 0
