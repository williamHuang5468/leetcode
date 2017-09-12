# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def show(self):
        node = self
        while(node is not None):
            print(node.val)
            node = node.next


class Solution(object):
    def removeElements(self, head, val):
        head, head.next = Node(0), head  # 建立頭節點，為了處理首節點是待刪除的值
        cur_node = head
        while(cur_node.next):
            if(cur_node.next.val is val):
                cur_node.next = cur_node.next.next  # 跳過刪除的值
            else:
                cur_node = cur_node.next  # 移動到下一個節點
        return head.next  # 跳過第一個節點(Node(0))


# 節點 5 -> 3
# 刪除 3
simple = Node(5)
simple.next = Node(3)
s = Solution()
node = s.removeElements(simple, 5)
node.show()

# 節點 1
# 刪除 1
one = Node(1)
node = s.removeElements(one, 1)
if(node is None):
    print("None")
