# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:34:11 2018

@author: Tsingzao
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    nb = [(i-1,j), (i+1,j), (i, j-1), (i, j+1)]
                    for x, y in nb:
                        if x<0 or y<0 or x==len(grid) or y==len(grid[0]) or grid[x][y] == 0:
                            ret = ret + 1
        return ret