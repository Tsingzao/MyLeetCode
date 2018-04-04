# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 17:06:46 2018

@author: Tsingzao
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            if nums[0]==0:
                return 1
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>1:
                return i
        return i+1