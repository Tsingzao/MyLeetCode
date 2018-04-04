# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 17:19:37 2018

@author: Tsingzao
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = list(set(nums))
        temp.sort()
        if len(temp)<3:
            return temp[-1]
        return temp[-3]