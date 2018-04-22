# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 17:39:24 2018

@author: Tsingzao
"""

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        temp[:] = nums[:]
        temp = sorted(temp)
        if len(temp) == 1:
            return 0
        if len(temp) >= 2:
            if (temp[-2] == 0) or (temp[-2] != 0 and temp[-1] / temp[-2] >= 2):
                return nums.index(temp[-1])
        return -1