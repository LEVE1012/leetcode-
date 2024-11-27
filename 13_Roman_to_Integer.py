#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#I can be placed before V (5) and X (10) to make 4 and 9. 

#X can be placed before L (50) and C (100) to make 40 and 90. 

#C can be placed before D (500) and M (1000) to make 400 and 900.

#Given a roman numeral, convert it to an integer.

class Solution(object):
    def romanToInt(self, s):
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        lenth = len(s)

        for i in range(lenth - 1):
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                res -= roman_map[s[i]]
            else:
                res += roman_map[s[i]]
        
        return res + roman_map[s[lenth - 1]]
        """
        :type s: str
        :rtype: int
        """

#和12题的思路一样，都是贪心算法，但是还是有很大差别的，
#这道题的思路非常巧妙，是通过前后的比较来判断是加还是减
#时间复杂度为O(n)，空间复杂度为O(1)
