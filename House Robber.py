# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:36:19 2018

@author: Tsingzao
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last+num, now)
        return now