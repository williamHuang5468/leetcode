class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        方法 - 用 Set 儲存節點進行比較：
        1. 用 set 存已經走過的 Node。
        2. 每次檢查 目前節點 是否存在 set 中。
        e.g. 5 -> 1 -> 2 -> 1 -> 2
        set : 5, 5 -> 1, 5 -> 1 -> 2
        當 節點 (1 -> 2) 存在於 set 回傳 True
        """
        nodeSet = set()
        while head is not None:
            if head in nodeSet:
                return True
            else:
                nodeSet.add(head)
            head = head.next
        return False
    '''
    def hasCycle(self, head):
        """
        方法 - 奔跑者方法：
        1. 用兩指針，快的和慢的，快的每次走兩步，慢的每次走一步
        2. 當快的和慢的相遇，值會相同。否則快的指針會遇到 None 做結束
        3. 最前面檢查兩個意外情況，head 是空的和 head 只有一個節點的情況
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow is not fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
    '''
    '''
    def hasCycle(self, head):
        """
        方法 - 用例外處理改良奔跑者方法：
        1. 將檢查 None 的行為，用例外處理解決。
        當遇到 None 會出現 `AttributeError`
        2. 這樣就只要檢查 慢指針 和 快指針相遇的情況，當不相遇的情況，由例外處理。
        """
        try:
            slow = head
            fast = head.next
            while(fast is not slow):
                slow = slow.next
                fast = fast.next.next
            return True
        except AttributeError:
            return False
    '''
