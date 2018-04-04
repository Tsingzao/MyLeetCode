# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 15:43:29 2018

@author: Tsingzao
"""

'''==============坑爹不能写nums=...================'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        nums[:] = nums[:len(nums)-k][::-1]+nums[len(nums)-k:][::-1]
        nums[:] = nums[::-1]