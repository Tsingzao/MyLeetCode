# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 08:47:20 2018

@author: Tsingzao
"""

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ct = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                ct = ct + 1
                if ct > 1 or ((i >= 1 and nums[i-1] > nums[i+1]) and (i < len(nums)-2) and nums[i+2] < nums[i]):
                    return False
        return True