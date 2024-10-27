# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        cnt = Counter()
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)  # 最长子串

        return ans


if __name__ == '__main__':
    _s = "abcabcbb"
    _solution = Solution()
    _ans = _solution.lengthOfLongestSubstring(s=_s)
    print(_ans)

    """
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
