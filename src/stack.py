class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def setNext(self, next_):
        self.next_node = next_


class Stack:
    """Класс для стека"""
    data_stack = []

    def __init__(self):
        """Конструктор класса Stack"""
        self.head = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

        self.data_stack.append(data)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        return self.data_stack.pop()

    @property
    def top(self):
        return self.head
