# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums=nums, target=target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = self.lower_bound(nums=nums, target=target + 1) - 1

        return [start, end]

    @staticmethod
    def lower_bound(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == '__main__':
    _nums = [5, 7, 7, 8, 8, 10]
    _target = 8

    _solution = Solution()
    _res = _solution.searchRange(nums=_nums, target=_target)
    print(_res)

    """
    时间复杂度: 数据不断被减半, 于是为O(logn)
    空间复杂度: 只使用了几个变量, 没有用到额外的变量, 所以为O(1)
    """
