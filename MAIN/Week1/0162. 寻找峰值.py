# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:  # 小于等于会出现mid+1的越界
            mid = left + (right - left) // 2
            if len(nums) <= 1:
                return 0
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == '__main__':
    # _nums = [1, 2, 1, 3, 5, 6, 4]
    # _nums = [1]
    _nums = [1, 2]
    _solution = Solution()
    _res = _solution.findPeakElement(nums=_nums)
    print(_res)
