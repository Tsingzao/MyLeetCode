# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 13:08:36 2018

@author: Tsingzao
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        cnt = 0
        cok = 0
        while cnt < len(g) and cok < len(s):
            if s[cok] >= g[cnt]:
                cnt = cnt + 1
            cok = cok + 1
        return cnt
