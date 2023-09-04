'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

例1：
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

例2：
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

例3：
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 若字符为空则，直接返回0
        if not s: return 0
        # 字符串开始index
        start = 0
        # 最长字符串长度
        max_len = 0
        # 当前字符串长度
        cur_len = 0
        # 使用集合确保无重复
        look_up = set()
        # 字符串总长度，用于控制循环
        num = len(s)
        # 滑动窗口，从0开始，每往后加一位，就判断下是否符合“不重复的限制条件”
        for stop in range(num):
            # 每加一位，当前字符串长度+1
            cur_len += 1
            while s[stop] in look_up:
                # 发现字符重复，只要重复字符还在，就会一直循环，直到将重复字符串之前的字符都移除掉
                look_up.remove(s[start])
                # 启始坐标+1
                start += 1
                # 当前字符串长度-1
                cur_len -= 1
            # 当现有字符串长度大于最大字符串长度，替换之
            if cur_len > max_len: max_len = cur_len
            # 若stop位置上的字符不重复，则将它添加到集合中
            look_up.add(s[stop])
        return max_len

    def getLongestSubstring(self, s: str) -> int:
        # 若字符为空则，直接返回0
        if not s: return "字符串为空"
        str_list = []   # 空list，用例存储所有不重复的字符串
        start = 0       # 字符串开始index
        look_up = []     # set存储是无序的，这里用list存储，确保字符串顺序与输入一致
        num = len(s)        # 字符串总长度，用于控制循环
        # 滑动窗口，从0开始，每往后加一位，就判断下是否符合“不重复的限制条件”
        for i in range(num):
            if s[i] in look_up:
                str_list.append(''.join(look_up))
            while s[i] in look_up:
                # 发现字符串重复，将重复字符串之前的字符都移除掉
                look_up.remove(s[start])
                # 启始坐标+1
                start += 1
            # 若stop位置上的字符不重复，则将它添加到集合中
            look_up.append(s[i])
        return max(str_list, key=len, default='')
        # return str_list


if __name__ == '__main__':
    s1 = "pwwkew"
    s2 = "abcabcbb"
    s3 = "abcbcbb"
    print(Solution().lengthOfLongestSubstring(s1))
    print(Solution().getLongestSubstring(s1))
    print(Solution().lengthOfLongestSubstring(s2))
    print(Solution().getLongestSubstring(s2))
    print(Solution().lengthOfLongestSubstring(s3))
    print(Solution().getLongestSubstring(s3))



    '''
    思考：
    1、获取的是最长字串的长度，长度，长度，需要遍历整个字符串后才能得出结果,最长字串的长度是通过max_len计算得到
    2、关键在于 "将重复字符串之前的字符都移除掉" ，这部分的设计使用set正好
    3、如果需要获得最长字串，字符串本身，则需要改造下，将set换成list
    '''
