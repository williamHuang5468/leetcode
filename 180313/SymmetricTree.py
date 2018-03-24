class TreeNode(object):
    def __init__(self, value= None):
        self.left = None
        self.right = None
        self.val = value

class Solution:
    def isSymmetric(self, root):
        """
        Answer one : use Recursively
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

    def isSymmetric(self, root):
        """
        Answer two : use Queue + BFS
        """
        if root is None:
            return True
        queue = collections.deque([root.left, root.right])
        
        while queue:
            leftNode, rightNode = queue.popleft(), queue.popleft() 
            if not leftNode and not rightNode:
                continue
            elif (not leftNode or not rightNode) or (leftNode.val != rightNode.val):
                return False
            
            queue += [leftNode.left, rightNode.right, leftNode.right, rightNode.left]
            
        return True
if __name__ == '__main__':
    pass

