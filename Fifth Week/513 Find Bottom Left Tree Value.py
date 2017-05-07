class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        for node in queue:
            if node.right != None:
                queue.append(node.right)
            if node.left != None:
                queue.append(node.left)
        return node.val

s = Solution()
t = TreeNode(2)
t.left = TreeNode(1)
t.right = TreeNode(3)
assert (s.findBottomLeftValue(t)) == 1