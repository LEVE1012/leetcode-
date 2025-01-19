#Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

#The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

#Return the quotient after dividing dividend by divisor.

#Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        sign = -1 if (dividend < 0) != (divisor < 0) else 1

        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp_divisor, num_divisions = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_divisions <<= 1
            dividend -= temp_divisor
            quotient += num_divisions
        
        result = sign * quotient
        return max(min(result, 2**31 - 1), -2**31)

  #用到了计算机组成原理中的位移运算，其中位移由计算机自动处理，无需刻意转换为二进制
