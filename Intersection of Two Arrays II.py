# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:54:13 2018

@author: Tsingzao
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1, n2 = collections.Counter(nums1), collections.Counter(nums2)
        return list((n1 & n2).elements())