# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

""" 两数之和II """

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:  # 有序数组, 相向双指针
            s = numbers[left] + numbers[right]
            if s == target:
                break
            if s > target:
                right -= 1
            else:
                left += 1

        return [left + 1, right + 1]


if __name__ == '__main__':
    _solution = Solution()
    _result = _solution.twoSum(numbers=[2, 7, 11, 15], target=9)
    print(_result)

    """
    时间复杂度: 每次遍历要么left+1要么right-1, 最坏的情况是两者加起来移动整个数组, 故为O(n)
    空间复杂度: 由于只用了几个变量, 所以空间复杂度是O(1)
    """