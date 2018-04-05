# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 18:02:18 2018

@author: Tsingzao
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) != r*c:
            return nums
        temp = []
        for i in xrange(len(nums)):
            temp = temp + nums[i]
        nums = []
        for i in xrange(r):
            nums.append(temp[i*c:(i+1)*c])
        return nums