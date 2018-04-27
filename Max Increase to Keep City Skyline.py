# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:36:07 2018

@author: Tsingzao
"""

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ltr = [max(line) for line in grid]
        ttb = [max(col[i] for col in grid) for i in range(len(grid[0]))]

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cnt += max(min(ltr[i]-grid[i][j],ttb[j]-grid[i][j]),0)
        return cnt