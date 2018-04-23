# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:33:12 2018

@author: Tsingzao
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses = sorted(houses)
        heaters = sorted(heaters) + [float('inf')]
        i = 0
        ret = 0
        for house in houses:
            while house >= sum(heaters[i:i+2])/2.:
                i = i + 1
            ret = max(ret, abs(heaters[i] - house))
        return ret
            