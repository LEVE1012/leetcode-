#Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0): 
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return reversed_half == x or reversed_half // 10 == x
        """
        :type x: int
        :rtype: bool
        """

#这道题思路还是比较重要的，首先是判断错误的条件，当 x < 0 or x 对 10 的余数为 0 且不为 0 时，可以直接判负
#其次是在运算过程中尽可能的节约时间，当一个数反转到一半的时候已经可以判断结果正负了
#另外在判断的时候，还要注意这个数的位数是奇数还是偶数，如果是偶数的话直接比较，奇数的话还需要将已反转的数除以 10 再去比较
#时间复杂度为O(log10(n))，空间复杂度为O(1)
