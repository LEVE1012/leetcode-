#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

#(you may want to display this pattern in a fixed font for better legibility)

#P   A   H   N
#A P L S I I G
#Y   I   R

#And then read line by line: "PAHNAPLSIIGYIR"

#Write the code that will take a string and make this conversion given a number of rows:

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        current_row = 0
        direction = -1
        rows = [""] * numRows

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            current_row += direction
        return "".join(rows)
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
      
#这道题没什么好说的，创建一个导向数，到达两边边界以后反转
#时间复杂度O(n)，空间复杂度O(n)
