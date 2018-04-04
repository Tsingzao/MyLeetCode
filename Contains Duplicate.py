# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 16:15:57 2018

@author: Tsingzao
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #key_value = {}
        #for num in nums:
        #    if not num in key_value:
        #        key_value[num] = 1
        #    else:
        #        key_value[num] = key_value[num] + 1
        #        if key_value[num] > 1:
        #            return True
        #return False
        
        return True if len(nums)!=len(set(nums)) else False