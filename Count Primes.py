# -*- coding: utf-8 -*-
"""
Created on Sun Apr 01 18:19:59 2018

@author: Tsingzao
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
            
        is_prime = [True]*n
        is_prime[0] = is_prime[1] = False
        
        for i in range(2,int(n**0.5)+1):
            if is_prime[i]:
                is_prime[i*i:n:i] = [False]*len(is_prime[i*i:n:i])
        return sum(is_prime)