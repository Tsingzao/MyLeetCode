# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 17:19:19 2018

@author: Tsingzao
"""

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        bd = int(area**(0.5))
        for w in range(bd,0,-1):
            if w*(area//w) == area:
                return [area//w, w]
        return []