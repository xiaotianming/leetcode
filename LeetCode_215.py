"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
"""
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, l, r):
            # 在（l,r）中选取随机数与nums[l]交换作为哨兵
            p = random.randint(l,r)
            nums[l], nums[p] = nums[p], nums[l]
            flag = nums[l]

            i, j = l, r
            while i < j:
                # 从后往前，比哨兵大的放右边
                while i < j and nums[j] >= flag:
                    j -= 1
                nums[i] = nums[j]
                # 从前往后，比哨兵小的放左边
                while i < j and nums[i] <= flag:
                    i += 1
                nums[j] = nums[i]
            # 最后i=j退出循环，待比较数据放入最终位置
            nums[i] = flag
            return i

        def quicksort(nums, l, r):
            if l >= r: return
            i = partition(nums, l, r)
            quicksort(nums, l, i - 1)
            quicksort(nums, i + 1, r)

        quicksort(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    print(s.findKthLargest(nums,k))

