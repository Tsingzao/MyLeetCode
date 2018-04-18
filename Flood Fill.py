# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:50:19 2018

@author: Tsingzao
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        def dfs(i, j):
            if (not (0<=i<len(image) and 0<=j<len(image[0]))) or image[i][j] != color:
                return
            image[i][j] = newColor
            for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                dfs(x,y)
        if color != newColor:
            dfs(sr, sc)
        return image