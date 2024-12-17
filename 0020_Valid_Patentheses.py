#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.

#Open brackets must be closed in the correct order.

#Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        stack = []
        bracket_map = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
        """
        :type s: str
        :rtype: bool
        """

#比较经典的括号匹配问题，使用堆栈来实现
#时间复杂度为O(n)，空间复杂度为O(n)
