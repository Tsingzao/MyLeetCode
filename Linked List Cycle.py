# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:19:51 2018

@author: Tsingzao
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        s = head
        f = head.next
        while f is not None and f.next is not None:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False