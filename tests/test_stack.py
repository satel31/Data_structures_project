import unittest

from src.stack import Node, Stack


class TestNode(unittest.TestCase):
    data_t = Node(5, 10)
    data_n = Node(5)

    def test_node_init(self):
        """Test of init function"""
        self.assertIs(self.data_t.data, 5)
        self.assertIs(self.data_t.next_node, 10)
        self.assertIsNone(self.data_n.next_node)


class TestSteck(unittest.TestCase):
    def test_stack_init(self):
        """Test of init function"""
        data_s = Stack()
        self.assertIsNone(data_s.top)

    def test_push(self):
        """Test of push function"""
        data_s = Stack()
        data_s.push(5)
        self.assertIsNot(data_s.top, None)

    def test_pop(self):
        """Test of pop function"""
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertIs(stack.pop(), 'data3')

    def test_str(self):
        """Test of str function"""
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(str(stack), 'Последний элемент: data3')

