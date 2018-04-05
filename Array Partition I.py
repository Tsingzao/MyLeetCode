# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 17:53:59 2018

@author: Tsingzao
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])