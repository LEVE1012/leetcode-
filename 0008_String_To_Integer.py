#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

#The algorithm for myAtoi(string s) is as follows:

#Whitespace: Ignore any leading whitespace (" ").
  
#Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
  
#Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. 

#If no digits were read, then the result is 0.

#Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. 

#Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

#Return the integer as the final result.

class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        if not s:
            return 0
        
        is_negative = 1
        if s[0] == '-':
            is_negative = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        
        result *= is_negative
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            result = INT_MIN
        elif result > INT_MAX:
            result = INT_MAX
        
        return result
        """
        :type s: str
        :rtype: int
        """

#这道题看似简单，实则还是有挺多的细节的，比如说在识别字符的时候，要考虑三种情况，加号，减号，还有数字，
#当是数字的时候，用 result 乘以 10 加上字符转 int 
#时间复杂度为O(n)，空间复杂度为O(1)
