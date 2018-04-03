# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 15:46:35 2018

@author: Tsingzao
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        last, i, j = m+n-1, m-1, n-1

        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[last] = nums1[i]
                i = i - 1
            else:
                nums1[last] = nums2[j]
                j = j - 1
            last = last - 1
            
        while j >= 0:
            nums1[last] = nums2[j]
            last, j = last - 1, j - 1
