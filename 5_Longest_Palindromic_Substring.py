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

#11.27重看
#我觉得有点丑陋哈哈哈哈，感觉这个条件像是这个人因为刚开始出错所以加上的一个墙壁，不过能做到这一步，由于每次都可以快速获取该字符串的初始回文半径，
#只通过加有限次的数量进而准确获取每个字符对应的最大半径，进而将时间复杂度控制在on感觉上是把所有能用的简化条件都压缩到极致了，
#我可以想到如果这个算法缺少了mirror这个比较关键的部分，就变成单纯的遍历一个数组进而很无聊了，如果变成单调的数组遍历，最复杂的情况（也就是只有一个字符构成的一个字符串），
#时间复杂度会变为on平方，而马拉车算法会将时间压缩，在遍历到中心部分的时候就能将right覆盖到最后，这样后续的一半就可以不用算了，而前面的一半也只需要进行有限次的加减即可。
#我后来又想了想，其实不管对称轴跑到哪里，由于它的产生的特殊性，导致我在以mirror和right-i为基础的情况下，最多只需要再扩展 两次 即可达到最大（这也是这个算法的奇妙之处），
#所以最后的情况其实就是on的复杂度而已，终究是以n的倍数计算的，甚至还可以在某些情况下比n都小，这就是把时间压缩到极致的艺术
#天呐，算法就是这么牛逼
