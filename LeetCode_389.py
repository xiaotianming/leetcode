"""
给定两个字符串 s 和 t ，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。
"""

# python3 ascii码
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) == 1:return t
        alist = [0] * 26
        for a in s:
            c = ord(a) - ord('a')
            alist[c] += 1
        for b in t:
            d = ord(b) - ord('a')
            if alist[d] == 0:
                return chr(d+97)
            alist[d] -= 1

# python3 字典
class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) == 1:
            return t
        dic = {}
        for w in s:
            if w not in dic:
                dic[w] = 1
            else:
                dic[w] += 1
        for y in t:
            if y in dic:
                dic[y] -= 1
                if dic[y] == 0:
                    del dic[y]
            else:
                dic[y] = 1
        for key in dic.keys():
            return key

if __name__ == '__main__':
    s = Solution()
    s1 = "abcd"
    t1 = "abcde"
    print(s.findTheDifference(s1, t1))