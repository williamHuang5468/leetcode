from SymmetricTree import Tree
from SymmetricTree import Node
import unittest

class TestNode(unittest.TestCase):
    def test_empty_node(self):
        n = Node()
        self.assertEqual(n.value, None)

    def test_root(self):
        n = Node(5)
        self.assertEqual(n.value, 5)

    def test_simple_tree(self):
        datas = [1,2,2]
        n = Tree(datas)
        self.assertEqual(n.root.value, 1)
        self.assertEqual(n.root.left.value, 2)
        self.assertEqual(n.root.right.value, 2)

if __name__ == '__main__':
    unittest.main()
