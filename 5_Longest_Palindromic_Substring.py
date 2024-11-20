#Given a string s, return the longest palindromic substring in s.

#动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 0
        
        for i in range(n):
            dp[i][i] = True  # 单字符回文
        
        for length in range(2, n + 1):  # 子串长度从 2 开始
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if length > max_len:
                            start = i
                            max_len = length
        
        return s[start:start + max_len]

#比较容易理解的一个方法，length 就是最终的字符的长度，i 是起点，j 是关于中心与 i 对称的点
#如果从i - 1到j - 1也是回文子串，且 i 和 j 对应的字符相等，那么从 i 到 j 也是回文子串
#时间复杂度为O(n^2)，空间复杂度为O(n^2)

#马拉车算法
class Solution(object):
    def longestPalindrome(self, s):
        t = '#' + '#'.join(s) + '#'
        n = len(t)

        p = [0] * n
        center, right = 0, 0
        max_len, start = 0, 0

        for i in range(n):
            if i < right:
                mirror = 2 * center - i
                p[i] = min(right - i, p[mirror])
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1
            
            if i + p[i] > right:
                center = i
                right = i + p[i]

            if p[i] > max_len:
                max_len = p[i]
                start = (i - max_len) // 2
        return s[start:start + max_len]
        """
        :type s: str
        :rtype: str
        """

#这个算法有点抽象，它将每个点位所对应的最长回文字符串记录为一个列表
#首先 i 是当前回文子串的中心，不断向外扩展，直到计算出最后的长度，并在 max_len 中进行更新
#其次就是优化时间的一个操作，如果 i 在 right 的范围内，就可以通过对称快速确定部分回文信息，无需重新计算
#这样一来每个字符只需要扩展一次，即可求出最终的最长回文子串
#时间复杂度为O(n), 空间复杂度为O(n)
