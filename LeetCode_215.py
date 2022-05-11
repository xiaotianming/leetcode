from random import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, l, r):
            # 在（l,r）中选取随机数与nums[l]交换作为哨兵
            p = nums[l]
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

