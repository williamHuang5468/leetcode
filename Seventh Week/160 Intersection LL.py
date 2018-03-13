# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        '''
        Two Pointer way
        '''
        if headA is None or headB is None:
            return None
        pointerA = headA
        pointerB = headB
        while(pointerA is not pointerB):  # 找到就停下來
            pointerA = headB if pointerA is None else pointerA.next
            pointerB = headA if pointerB is None else pointerB.next
        return pointerA
