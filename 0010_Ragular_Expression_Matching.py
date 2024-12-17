#Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

#'.' Matches any single character.​​​​

#'*' Matches zero or more of the preceding element.

#The matching should cover the entire input string (not partial).

class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        return dp[m][n]
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

#第二道hard类型的题目，递归或者动态规划是解决问题的关键，但是递归消耗的时间太长会导致过不了
#首先构建一个 dp 表，用来存储前 i 和 j 个字符是否匹配，接下来分别构建 '.', '*', 以及正常字符的判断逻辑
#时间复杂度为O(m * n)， 空间复杂度为O(m * n)
