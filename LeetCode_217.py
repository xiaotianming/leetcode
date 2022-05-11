"""
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false。
输入：nums = [1,2,3,1]
输出：true
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))