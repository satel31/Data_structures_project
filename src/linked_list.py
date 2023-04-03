class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data: dict, next_node=None) -> None:
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0


    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data)
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next_node = self.head
            self.head = node
        self.length += 1

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node
        self.length += 1

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def to_list(self) -> list:
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""
        node = self.head
        ll_list = []
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, id_key) -> dict:
        """Возвращает первый найденный в LinkedList словарь с ключом 'id'"""
        data = self.to_list()
        for d in data:
            try:
                if d['id'] == id_key:
                    return d
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")
