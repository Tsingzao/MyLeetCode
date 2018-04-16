# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:40:25 2018

@author: Tsingzao
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n-1):
            temp = []
            cnt = 1
            for idx in range(1,len(s)):
                if s[idx] == s[idx-1]:
                    cnt = cnt + 1
                else:
                    temp.append(str(cnt))
                    temp.append(s[idx-1])
                    cnt = 1
            temp.append(str(cnt))
            temp.append(s[-1])
            s = "".join(temp)

        return s