#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

#纵向比较法
def longest_common_prefix_vertical(strs):
    if not strs:
        return ""
    
    # 遍历每个字符索引
    for i in range(len(strs[0])):
        char = strs[0][i]  # 第一个字符串的当前字符
        for string in strs[1:]:
            # 如果超出当前字符串长度或者字符不同
            if i >= len(string) or string[i] != char:
                return strs[0][:i]
    
    return strs[0]  # 如果没有中途返回，说明第一个字符串是公共前缀


#二分查找法
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        def is_common_prefix(length):
            prefix = strs[0][:length]
            #检查数组中的所有字符串是否都以prefix开头
            return all(string.startswith(prefix) for string in strs)
        
        min_len = min(len(s) for s in strs)
        low, high = 0, min_len

        while low < high:
            mid = (low + high + 1) // 2
            if is_common_prefix(mid):
                low = mid
            else:
                high = mid - 1
        
        return strs[0][:low]


#排序法
def longest_common_prefix_sort(strs):
    if not strs:
        return ""
    
    # 排序字符串数组
    strs.sort()
    first = strs[0]
    last = strs[-1]
    
    # 比较第一个和最后一个字符串的公共前缀
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    
    return first[:i]


#分治法
def longest_common_prefix_divide_and_conquer(strs):
    def common_prefix(left, right):
        # 比较两个字符串的公共前缀
        min_len = min(len(left), len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[:i]
        return left[:min_len]
    
    def divide_and_conquer(l, r):
        if l == r:
            return strs[l]  # 只有一个字符串时，返回它自身
        mid = (l + r) // 2
        left_prefix = divide_and_conquer(l, mid)
        right_prefix = divide_and_conquer(mid + 1, r)
        return common_prefix(left_prefix, right_prefix)
    
    if not strs:
        return ""
    
    return divide_and_conquer(0, len(strs) - 1)

#具体时间复杂度设计的因素有点多，
#简单高效的场景：推荐 纵向扫描法 或 排序法。
#需要递归或分布式思路：分治法更适合。
#大规模数据，且字符串较短：二分查找法是最优选择。
