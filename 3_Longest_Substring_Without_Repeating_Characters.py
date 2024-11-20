#Given a string s, find the length of the longest 
#substring
#without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        max_length = 0
        start = 0
        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = end
            max_length = max(max_length, end - start + 1)
        return max_length
        """
        :type s: str
        :rtype: int
        """
#这段程序主要是通过跳跃实现搜索的简化，如果一个字符在前面已经出现过，那么就修改它的索引的同时，修改start，也就是起始位置，进而实现字符之间的跳跃，简化了搜索的步骤
#时间复杂度为O(n)，空间复杂度为O(n)
