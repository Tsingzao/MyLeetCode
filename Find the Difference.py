# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:10:29 2018

@author: Tsingzao
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ss = collections.Counter(s)
        tt = collections.Counter(t)
        for temp in tt:
            if not temp in ss:
                return temp
            else:
                if tt[temp] != ss[temp]:
                    return temp
        
#==============================================================================
#         return list((collections.Counter(t) - collections.Counter(s)))[0]
#==============================================================================
