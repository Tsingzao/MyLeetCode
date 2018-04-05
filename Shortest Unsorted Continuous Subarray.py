# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 18:21:45 2018

@author: Tsingzao
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        temp = []
        temp[:] = nums[:]
        temp.sort()
        i = 0 
        j = len(temp)-1
        while i < j:
            if nums[i] == temp[i]:
                i = i + 1
            if nums[j] == temp[j]:
                j = j - 1
            if nums[i] != temp[i] and nums[j] != temp[j]:
                break
        if i == j:
            return 0
        else:
            return j-i+1