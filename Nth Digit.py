# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:44:39 2018

@author: Tsingzao
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
#==============================================================================
#         temp = 0
#         num = 0
#         while temp < n:
#             num = num + 1
#             temp = temp + len(str(num))
#         if temp == n:
#             return int(str(num)[-1])
#         else:
#             return int(str(num)[-(temp-n+1)])
#==============================================================================

        start, width, count = 1, 1, 9
        while n > width * count:
            n = n - width * count
            start = start * 10
            count = count * 10
            width= width + 1
        return int(str(start + (n-1) // width)[(n-1)%width])
