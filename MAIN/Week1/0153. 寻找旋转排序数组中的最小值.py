# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1  # 因为nums[mid]严格大于nums[right], 说明nums[mid]一定不是最小值
            else:  # nums[mid]小于等于nums[right], 说明mid可能是最小值, 后者最小值在mid的左边
                right = mid

        return nums[left]


if __name__ == '__main__':
    _nums = [4, 5, 6, 7, 0, 1, 2]
    _solution = Solution()
    _res = _solution.findMin(nums=_nums)
    print(_res)
