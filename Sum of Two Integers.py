# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 21:16:13 2018

@author: Tsingzao
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
    
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a^b)&mask, ((a&b)<<1)&mask
        return a if a <= MAX else ~(a^mask)

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        else:
            return self.getSum(a^b, (a&b)<<1)
        

    def isPowerOfFour(self, n):
        """
        :tpye n: int
        :rtype: bool
        """
        return not (n&(n-1)) & (n&0x55555555)

    
    def countOnes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            n = n & (n-1)
            cnt += 1
        return cnt
