# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

""" 二分法
返回有序数组中第一个大于等于target的数的位置, 如果所有数都小于target, 则返回数组长度.
"""

from typing import List


def lower_bound(nums: List[int], target: int):
    """ 闭区间 """
    left = 0
    right = len(nums) - 1
    while left <= right:  # 区间不为空
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


if __name__ == '__main__':
    _nums = [5, 7, 7, 8, 8, 10]
    _target = 8

    _res = lower_bound(nums=_nums, target=_target)
    print(_res)
