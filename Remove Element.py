# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 09:54:45 2018

@author: Tsingzao
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums==[]:
            return 0
        i = 0
        while 1:
            if nums[i] == val:
                nums[i:-1] = nums[i+1:]
                nums[-1] = val
            else:
                i = i+1
            if i==len(nums)-nums.count(val):
                break
        return len(nums)-nums.count(val)   
