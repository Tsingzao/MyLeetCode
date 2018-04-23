# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:43:42 2018

@author: Tsingzao
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low <= high:
            mid = (low+high) / 2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                high = mid - 1
            else:
                low = mid + 1
        return mid