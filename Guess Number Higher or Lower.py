# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 10:58:50 2018

@author: Tsingzao
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low <= high:
            mid = (low+high)//2
            if guess(mid) > 0:
                low = mid + 1
            if guess(mid) < 0:
                high = mid - 1
            if guess(mid) == 0:
                return mid
            