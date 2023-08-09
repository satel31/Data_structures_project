from src.stack import Node, Stack

if __name__ == '__main__':
    stack = Stack()
    stack.push('data1')
    data = stack.pop()

    # Stack became empty
    assert stack.top is None

    # pop() deletes elements and return data
    assert data == 'data1'

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()

    assert stack.top.data == 'data1'

    assert data == 'data2'
