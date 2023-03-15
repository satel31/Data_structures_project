class Node:
    """Класс для узла стека"""

    def __init__(self, data: str, next_node=None) -> None:
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self) -> None:
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data: str) -> None:
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.top = Node(data, self.top)

    def pop(self) -> str:
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        deleted_element = self.top.data
        self.top = self.top.next_node
        return deleted_element

    def __str__(self) -> str:
        """Поскольку в main.py не указано, что должно возвращаться, я указала данные на свой выбор """
        return f'Последний элемент: {self.top.data}'


