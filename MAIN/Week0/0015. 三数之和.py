# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

""" 三数之和 """

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue
            if x + nums[i + 1] + nums[i + 2] > 0:
                break
            if x + nums[-1] + nums[-2] < 0:
                continue
            j = i + 1  # j是中间的数
            k = n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:  # j的上一个数是j - 1
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:  # k的上一个数是k + 1
                        k -= 1
        return ans


if __name__ == '__main__':
    _solution = Solution()
    _res = _solution.threeSum(nums=[-1, 0, 1, 2, -1, -4])
    print(_res)

    """
    时间复杂度: 排序时间复杂度是O(nlogn), for 和 while 是O(n^2), 所以总的时间复杂度是O(n^2)
    空间复杂度: 没有用到额外变量, 空间复杂度为O(1).
    """
