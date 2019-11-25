# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        max = 0
        max2 = 0
        for strIndex, strItem in enumerate(s):
            if strItem in dic:
                print(s[strIndex:])
                max = self.lengthOfLongestSubstring(Solution,s[dic[strItem]+1:])
                break
            else:
                dic[strItem] = strIndex
                if max2 < len(dic):
                    max2 = len(dic)

        if max < max2:
            max = max2
        print(max)
        return max

    def de_duplication(self,str):
        dedup_str = ''
        for char in str:
            if not char in dedup_str:
                dedup_str += char

        return dedup_str


    def lengthOfLongestSubstring2(self, s: str) -> int:
        i = 2
        flag = True
        while(flag):
            flag = False
            for j in range(len(s)-i+1):

                 if len(s[j:j+i]) == len(self.de_duplication(self,s[j:j+i])):
                     flag = True
            if flag :
                i+=1
        i -= 1
        print(i)
        return i



Solution.lengthOfLongestSubstring2(Solution,'aavv3s334425678')#