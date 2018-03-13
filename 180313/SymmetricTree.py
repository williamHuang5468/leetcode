class Node(object):
    def __init__(self, value= None):
        self.left = None
        self.right = None
        self.value = value

class Tree(object):
    def __init__(self, datas):
        node = Node(1)
        leftNode = Node(2)
        rightNode = Node(2)
        node.left = leftNode
        node.right = rightNode
        self.root = node

if __name__ == '__main__':
    pass

