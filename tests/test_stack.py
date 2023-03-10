import unittest

from src.stack import Node, Stack


class TestNode(unittest.TestCase):
    data_t = Node(5, 10)
    data_n = Node(5)

    def test_node_init(self):
        self.assertIs(self.data_t.data, 5)
        self.assertIs(self.data_t.next_node, 10)
        self.assertIsNone(self.data_n.next_node)

    def test_setNext(self):
        self.data_t.setNext(13)
        self.assertIs(self.data_t.next_node, 13)


class TestSteck(unittest.TestCase):
    def test_stack_init(self):
        data_s = Stack()
        self.assertIsNone(data_s.head)

    def test_push(self):
        data_s = Stack()
        data_s.push(5)
        self.assertIsNot(data_s.head, None)

    def test_top(self):
        data_s = Stack()
        self.assertIsNone(data_s.top)

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertIs(stack.pop(), 'data3')
