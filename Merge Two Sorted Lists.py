# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 22:49:59 2018

@author: Tsingzao
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
def print_list(node):
    while node is not None:
        print node.val      
        node = node.next
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
l1 = a
a.next = b
b.next = c
a = ListNode(1)
b = ListNode(3)
c = ListNode(4)
l2 = a
a.next = b
b.next = c

print l1.val, l1.next.val, l1.next.next.val
print l2.val, l2.next.val, l2.next.next.val

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = ListNode(None)
        ret = cur
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 or l2      
        return ret.next