# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, node):
        self.next = node


class Solution(object):
    def sortList(self, head):
        head, head.next = Node(0), head
        prev = head
        cur = head.next # 3
        runner = head.next.next # 2
        while(runner is not None):
            if(runner.val < cur.val):
                copyNewNode = cur # 3
                copyNewNode.next = None # 3 -> None
                copyNextNode = runner # 2
                copyNextNode.next = copyNewNode # 2 -> 3 -> None
                prev.next = copyNextNode # 0 -> 2 -> 3 -> None
                runner = runner.next # 2 -> 1
            else:
                prev = cur
                cur = cur.next
        return head.next


f = Node(3)
sec = Node(2)
sec.add(Node(1))
f.add(sec)

s = Solution()
a = s.sortList(f)
while(a is not None):
    print(a.val)
    a = a.next
