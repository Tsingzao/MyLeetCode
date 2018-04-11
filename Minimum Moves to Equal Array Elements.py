# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 22:55:17 2018

@author: Tsingzao
"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums)*len(nums)