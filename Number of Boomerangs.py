# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:16:03 2018

@author: Tsingzao
"""

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        num = 0
        for p in points:
            c = {}
            for q in points:
                dis = (p[0]-q[0])**2+(p[1]-q[1])**2
                c[dis] = 1 + c.get(dis, 0)
            for k in c:
                num = num + c[k]*(c[k]-1)
        return num