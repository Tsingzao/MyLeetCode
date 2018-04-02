# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 15:16:15 2018

@author: Tsingzao
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
                break
        return i+1
