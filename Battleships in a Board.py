# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:17:26 2018

@author: Tsingzao
"""

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ret = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    flag = 1
                    if j > 0 and board[i][j-1] == 'X':
                        flag = 0
                    if i > 0 and board[i-1][j] == 'X':
                        flag = 0
                    ret += flag
        return ret