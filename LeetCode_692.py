"""
给定一个单词列表words和一个整数 k ，返回前k个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。



示例 1：

输入: words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。

"""
import collections
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash = collections.Counter(words)
        res = sorted(hash, key=lambda word: (-hash[word], word))
        return res[:k]

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))

