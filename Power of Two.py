# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:03:56 2018

@author: Tsingzao
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
#==============================================================================
#         if n == 0:
#             return False
#         while n == round(n) and n != 1:
#             n = n / 2.
#         if n == 1:
#             return True
#         else:
#             return False
#==============================================================================

        '''
        Power of 2 means only one bit of n is ‘1’, so use the trick n&(n-1)==0 
        to judge whether that is the case
        '''
        if n <= 0:
            return False
        return not n&(n-1)