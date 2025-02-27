from src.queue import Queue

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    assert queue.dequeue() == 'data1'
    assert queue.dequeue() == 'data2'
    assert queue.dequeue() == 'data3'
    assert queue.dequeue() is None
