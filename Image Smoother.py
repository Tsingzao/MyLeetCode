# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 23:07:11 2018

@author: Tsingzao
"""

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        from copy import deepcopy as copy
        x_len = len(M)
        y_len = len(M[0]) if x_len else 0
        res = copy(M)
        for x in range(x_len):
            for y in range(y_len):
                neighbors = [
                    M[_x][_y]
                    for _x in (x-1, x, x+1)
                    for _y in (y-1, y, y+1)
                    if 0 <= _x < x_len and 0 <= _y < y_len
                ]
                res[x][y] = sum(neighbors) // len(neighbors)
        return res