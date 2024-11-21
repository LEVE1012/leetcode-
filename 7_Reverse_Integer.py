#Given a signed 32-bit integer x, return x with its digits reversed. 

#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution(object):
    def reverse(self, x):
        result, current = 0, 0
        is_negative = x < 0
        x = abs(x)
      
        while x != 0:
            current = x % 10 
            x = x // 10
            result = result * 10 + current
        
        if result > 2**31 - 1:
            return 0
        else:
            return -result if is_negative else result
        """
        :type x: int
        :rtype: int
        """
#相对简单的一道题，也可以采用反转字符串的方法，看起来可能更简洁
#时间复杂度为O(log10(n))，空间复杂度为O(1)

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x < 0
        x = abs(x)
      
        reversed_str = str(x)[::-1] #反向从头到尾读取数组，存入reversed_str中
        result = int(reversed_str)

        if result > 2**31 - 1:
            return 0

        return -result if is_negative else result
#时间复杂度为O(log10(n))，空间复杂度为O(log10(n))
