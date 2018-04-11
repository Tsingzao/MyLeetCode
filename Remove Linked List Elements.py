# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:43:07 2018

@author: Tsingzao
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = ListNode(None)
        temp.next = head
        pre = temp
        cur = head
        while cur is not None:
            if cur.val == val:
                pre.next = cur.next
                cur = cur.next
                continue
            pre = pre.next
            cur = cur.next
        return temp.next