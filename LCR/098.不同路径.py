# -*- coding: utf-8 -*-
# -*- author: jeremysun1224 -*-


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]  # 初始化
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


if __name__ == '__main__':
    _m, _n = 3, 7

    _solution = Solution()
    _path_num = _solution.uniquePaths(m=_m, n=_n)
    print(_path_num)
