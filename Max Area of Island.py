# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:59:11 2018

@author: Tsingzao
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = []
        def dfs(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i, j-1) + dfs(i,j+1)
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    temp = dfs(i,j)
                    ret.append(temp)
                    #if ret > temp:
                    #    ret = temp
        return max(ret) if ret else 0