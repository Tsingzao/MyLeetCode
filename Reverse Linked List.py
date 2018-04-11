# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 09:53:01 2018

@author: Tsingzao
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return pre