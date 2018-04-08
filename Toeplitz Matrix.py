# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 17:00:38 2018

@author: Tsingzao
"""

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in xrange(1,len(matrix)):
            for j in xrange(1,len(matrix[0])):
                if matrix[i][j]!=matrix[i-1][j-1]:
                    return False
        return True