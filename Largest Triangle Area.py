# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:52:26 2018

@author: Tsingzao
"""

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        area = 0
        num = len(points)
        for i in range(num-2):
            for j in range(i+1,num-1):
                for k in range(j+1,num):
                    area = max([area,abs(points[i][0]*points[j][1]+points[j][0]*points[k][1]+points[k][0]*points[i][1]
                               -points[i][0]*points[k][1]-points[j][0]*points[i][1]-points[k][0]*points[j][1])/2.])
        return area