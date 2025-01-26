class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or len(words[0]) == 0:
            return []
        
        word_len = len(words[0])
        word_count = Counter(words)
        n = len(words)
        total_len = word_len * n

        result = []

        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    current_count[word] += 1
                    count += 1

                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == n:
                        result.append(left)
                
                else:
                    current_count.clear()
                    count = 0
                    left = right
        return result
#同样长的的一个单词列表，求取列表中所有单词出现一次并组合成一个单词串的头索引序列，使用滑动窗口完成
