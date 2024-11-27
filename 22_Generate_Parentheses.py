#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(current_str, left, right):
            if len(current_str) == n * 2:
                result.append(current_str)
                return

            if left < n:
                backtrack(current_str + '(', left + 1, right)

            if right < left:
                backtrack(current_str + ')', left, right + 1) 

        backtrack("", 0, 0)
        
        return result
        """
        :type n: int
        :rtype: List[str]
        """

#这道题也是通过回溯的算法来实现的，其实铜鼓两道回溯题大致上也可以总结出一些经验
#首先是回溯必须有一个终止条件，常常是长度达到目标后停止，并把临时产生的变量加到最终的结果中
#其次是会有一些条件的约束，如果条件比较简单，可以直接通过排列组合的方法，先递归再pop掉来准备之后的递归
