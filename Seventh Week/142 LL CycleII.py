# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        '''
        用 set 去存 node ，去檢查 head 有沒有在 set 中
        '''
        nodeSet = set()
        while(head is not None):
            if(head in nodeSet):
                return head
            else:
                nodeSet.add(head)
            head = head.next
        return None
