# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        s = 0
        left = 0
        for right, x in enumerate(nums):
            s += x
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                ans = min(ans, right - left + 1)

        return ans if ans <= n else 0


if __name__ == '__main__':
    _solution = Solution()
    _ans = _solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3])
    print(_ans)

    """
    时间复杂度: O(n)
    空间复杂度: O(1)
    """