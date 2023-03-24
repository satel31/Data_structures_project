class Node:
    """Класс для узла очереди"""

    def __init__(self, data: str, next_node=None) -> None:
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self) -> None:
        """Конструктор класса Queue"""
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, data: str) -> None:
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        if self.length == 0:
            self.head = self.tail = node
        else:
            last = self.tail
            last.next_node = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.length == 0:
            return None
        first = self.head.data
        self.head = self.head.next_node
        self.length -= 1
        return first

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        if self.length == 0:
            return ""
        return f'{self.head.data}\n{self.head.next_node.data}\n{self.tail.data}'
