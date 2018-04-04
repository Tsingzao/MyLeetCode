# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 17:15:27 2018

@author: Tsingzao
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        z = 0
        while i < len(nums)-z:
            if nums[i]==0:
                nums[i:]=nums[i+1:]+[0]
                z = z + 1
            else:
                i = i + 1