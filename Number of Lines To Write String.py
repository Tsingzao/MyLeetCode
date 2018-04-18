# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:26:51 2018

@author: Tsingzao
"""

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        total = 0
        lines = 1
        for ss in S:
            total = total + widths[ord(ss)-ord('a')]
            if total > 100:
                total = widths[ord(ss)-ord('a')]
                lines = lines + 1
        return [lines, total]