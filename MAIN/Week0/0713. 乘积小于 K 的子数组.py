# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        prod = 1
        left = 0
        for right, x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1

        return ans


if __name__ == '__main__':
    _nums = [10, 5, 2, 6]
    _k = 100

    _solution = Solution()
    _ans = _solution.numSubarrayProductLessThanK(nums=_nums, k=_k)
    print(_ans)
