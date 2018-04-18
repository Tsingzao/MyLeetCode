# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 10:46:29 2018

@author: Tsingzao
"""

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def isPrime(num):
            if num < 2:
                return False
            for n in range(2,int(num**(0.5))+1):
                if num%n == 0:
                    return False
            return True
        cnt = 0
        for num in range(L, R+1):
            num = bin(num).count('1')
            if isPrime(num):
                cnt = cnt + 1
        return cnt