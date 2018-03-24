class TreeNode(object):
    def __init__(self, value= None):
        self.left = None
        self.right = None
        self.val = value

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.visit(root.left, root.right)
    
    def visit(self, left , right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        isEqual = left.val == right.val
        isLeftEqual = self.visit(left.left, right.right)
        isRightEqual = self.visit(left.right, right.left)
        return isEqual and isLeftEqual and isRightEqual

if __name__ == '__main__':
    pass

