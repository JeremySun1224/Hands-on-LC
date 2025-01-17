# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        result += 1
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:
                        result += 1
                        dp[i][j] = True
        return result


if __name__ == '__main__':
    _solution = Solution()
    _count = _solution.countSubstrings(s="abccba")
    print(_count)

