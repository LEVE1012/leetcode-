#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        def build_prefix_table(needle):
            m = len(needle)
            prefix = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and needle[i] != needle[j]:
                    j = prefix[j - 1]
                if needle[i] == needle[j]:
                    j += 1
                prefix[i] = j
            return prefix
        
        n, m = len(haystack), len(needle)
        prefix = build_prefix_table(needle)
        j = 0

        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = prefix[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1

  #使用了kmp算法，需要记忆
