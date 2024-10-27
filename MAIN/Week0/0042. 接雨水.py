# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """时间复杂度: O(n), 空间复杂度: O(n) """
        ans = 0
        n = len(height)
        pre_max = [height[0]] * n
        suf_max = [height[-1]] * n
        for i in range(1, n, 1):  # 前缀最大值
            pre_max[i] = max(height[i], pre_max[i - 1])
        for i in range(n - 2, -1, -1):  # 后缀最大值
            suf_max[i] = max(height[i], suf_max[i + 1])

        for h, p, s in zip(height, pre_max, suf_max):
            ans += min(p, s) - h

        return ans

    # def trap(self, height: List[int]) -> int:
    #     """ 时间复杂度: O(n), 空间复杂度: O(1) """
    #     n = len(height)
    #     ans = 0
    #     left = 0
    #     right = n - 1
    #     pre_max = 0
    #     suf_max = 0
    #     while left <= right:  # 相向双指针
    #         pre_max = max(pre_max, height[left])
    #         suf_max = max(suf_max, height[right])
    #         if pre_max < suf_max:
    #             ans += pre_max - height[left]
    #             left += 1
    #         else:
    #             ans += suf_max - height[right]
    #             right -= 1
    #     return ans


if __name__ == '__main__':
    _solution = Solution()
    _ans = _solution.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(_ans)
