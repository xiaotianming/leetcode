"""
给定数组people。people[i]表示第 i个人的体重，船的数量不限，每艘船可以承载的最大重量为limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为limit。

返回 承载所有人所需的最小船数。
示例 1：

输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)
"""
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = sorted(people)
        s = 0
        t = len(p) - 1
        count = 0
        while s <= t:
            if s == t:
                count += 1
                return count
            if p[t] + p[s] > limit:
                count += 1
                t -= 1
            else:
                s += 1
                t -= 1
                count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    people = [1,2]
    limit = 3
    print(s.numRescueBoats(people, limit))
