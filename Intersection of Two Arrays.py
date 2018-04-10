# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:32:53 2018

@author: Tsingzao
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return [x for x in set(nums2) if x in nums1]