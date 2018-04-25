# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:52:23 2018

@author: Tsingzao
"""

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        if n==2: 
            return 987
        #maxnum = 10**n-1
        #minnum = maxnum/10
        #thresh = int(minnum**(0.5))
        #for i in xrange(maxnum,minnum,-1):
        #    num = int(str(i)+str(i)[::-1])
        #    for j in xrange(maxnum,thresh,-1):
        #        if num/j>maxnum:
        #            break
        #        if num%j == 0:
        #            return num%1337
        #return 0
    
        for a in xrange(2, 9*10**(n-1)):
            hi=(10**n)-a
            lo=int(str(hi)[::-1])
            if a**2-4*lo < 0: continue
            if (a**2-4*lo)**.5 == int((a**2-4*lo)**.5):
                return (lo+10**n*(10**n-a))%1337