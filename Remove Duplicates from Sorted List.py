# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:10:52 2018

@author: Tsingzao
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        f, l = head, head.next if head else None
        while l:
            if f.val == l.val:
                l = l.next
                f.next = l
            else:
                f = l
                l = l.next
        return head