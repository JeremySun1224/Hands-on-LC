# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            ans = max(ans, area)

        return ans


if __name__ == '__main__':
    _solution = Solution()
    _ans = _solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(_ans)

    """
    时间复杂度: 每次移动一个指针, 花费O(1)的时间, 总计移动n次, 故时间复杂度是O(n)
    空间复杂度: 没有引入额外变量, 故空间复杂度为O(1)
    """
