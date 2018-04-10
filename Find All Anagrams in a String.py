# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:32:09 2018

@author: Tsingzao
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pp = collections.Counter(p)
        # return [i for i in range(len(s)-len(p)+1) if pp == collections.Counter(s[i:i+len(p)])]
        r = []
        ss = collections.Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            ss[s[i]] = ss[s[i]] + 1
            if ss == pp:
                r.append(i-len(p)+1)
            ss[s[i-len(p)+1]] = ss[s[i-len(p)+1]] - 1
            if ss[s[i-len(p)+1]] == 0:
                del ss[s[i-len(p)+1]]
        return r