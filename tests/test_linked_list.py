import unittest

from src.linked_list import Node, LinkedList


class TestNode(unittest.TestCase):
    data_t = Node(5, 10)
    data_n = Node(5)

    def test_node_init(self):
        """Test of init function"""
        self.assertIs(self.data_t.data, 5)
        self.assertIs(self.data_t.next_node, 10)
        self.assertIsNone(self.data_n.next_node)


class TestLinkedList(unittest.TestCase):
    def test_ll_init(self):
        """Test of init function"""
        data_l = LinkedList()
        self.assertEqual(data_l.length, 0)
        self.assertIsNone(data_l.head)
        self.assertIsNone(data_l.tail)

    def test_ll_insert_beginning_empty(self):
        """Test of insert_beginning function with empty list"""
        data_l = LinkedList()
        data_l.insert_beginning({'id': 1})
        self.assertEqual(data_l.head.data, {'id': 1})
        self.assertEqual(data_l.tail.data, {'id': 1})
        self.assertIsNone(data_l.tail.next_node)
        self.assertEqual(data_l.length, 1)

    def test_ll_insert_beginning_not_empty(self):
        """Test of insert_beginning function with not empty list"""
        data_l = LinkedList()
        data_l.insert_beginning({'id': 1})
        data_l.insert_beginning({'id': 2})
        self.assertEqual(data_l.tail.data, {'id': 1})
        self.assertEqual(data_l.head.next_node.data, {'id': 1})
        self.assertEqual(data_l.length, 2)

    def test_ll_insert_at_end_empty(self):
        """Test of insert_at_end function with empty list"""
        data_l = LinkedList()
        data_l.insert_beginning({'id': 1})
        self.assertEqual(data_l.head.data, {'id': 1})
        self.assertEqual(data_l.tail.data, {'id': 1})
        self.assertIsNone(data_l.tail.next_node)
        self.assertEqual(data_l.length, 1)

    def test_ll_insert_at_end_function_not_empty(self):
        """Test of insert_at_end function with not empty list"""
        data_l = LinkedList()
        data_l.insert_at_end({'id': 1})
        data_l.insert_at_end({'id': 2})
        self.assertEqual(data_l.tail.data, {'id': 2})
        self.assertIsNone(data_l.tail.next_node)
        self.assertEqual(data_l.length, 2)

    def test_ll_str_empty(self):
        """Test of str function with empty list"""
        ll = LinkedList()
        self.assertEqual(str(ll), "None")

    def test_ll_str_not_empty(self):
        """Test of str function with not empty list"""
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")
