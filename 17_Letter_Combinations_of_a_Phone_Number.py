#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

#A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        digit_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        result = []

        def back_track(index, current_combination):
            if index == len(digits):
                result.append("".join(current_combination))
                return
            letters = digit_map[digits[index]]

            for letter in letters:
                current_combination.append(letter) 
                back_track(index + 1, current_combination)
                current_combination.pop()
        back_track(0, [])
        return result
        """
        :type digits: str
        :rtype: List[str]
        """

#DFS算法，时间复杂度为O(4^n)，是回溯算法的典型时间复杂度，空间复杂度为O(n)，而且是一个临时占用的空间
#像钥匙开门一样，打不开就换一把
#有几个点需要注意，一个是终止条件是 index = len(digits) 而不是长度减一，另外就是当为空时需要直接返回不然会带双引号，最后就是一些语法规则也需要注意
