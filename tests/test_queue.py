import unittest

from src.queue import Node, Queue


class TestNode(unittest.TestCase):
    data_t = Node(5, 10)
    data_n = Node(5)

    def test_node_init(self):
        """Test of init function"""
        self.assertIs(self.data_t.data, 5)
        self.assertIs(self.data_t.next_node, 10)
        self.assertIsNone(self.data_n.next_node)

class TestQueue(unittest.TestCase):
    def test_queue_init(self):
        """Test of init function"""
        data_q = Queue()
        self.assertEqual(data_q.length, 0)
        self.assertIsNone(data_q.head)
        self.assertIsNone(data_q.tail)

    def test_queue_enqueue_empty(self):
        """Test of enqueue function with empty queue"""
        data_q = Queue()
        data_q.enqueue('data1')
        self.assertEqual(data_q.head.data, 'data1')
        self.assertEqual(data_q.tail.data, 'data1')
        self.assertIsNone(data_q.tail.next_node)
        self.assertEqual(data_q.length, 1)

    def test_queue_enqueue_not_empty(self):
        """Test of enqueue function with not empty queue"""
        data_q = Queue()
        data_q.enqueue('data1')
        data_q.enqueue('data2')
        self.assertEqual(data_q.tail.data, 'data2')
        self.assertEqual(data_q.head.next_node.data, 'data2')
        self.assertEqual(data_q.length, 2)

    def test_queue_str(self):
        """Test of str function"""
        data_q = Queue()
        self.assertEqual(str(data_q), "")
        data_q.enqueue('data1')
        data_q.enqueue('data2')
        data_q.enqueue('data3')
        self.assertEqual(str(data_q),"data1\ndata2\ndata3")





