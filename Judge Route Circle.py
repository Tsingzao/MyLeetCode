# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:48:17 2018

@author: Tsingzao
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R')