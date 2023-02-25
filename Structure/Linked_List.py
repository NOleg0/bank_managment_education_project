class LinkedList:
    class LinkedListElement:
        def __init__(self, data, next_node = None):
            self.data = data
            self.next_node = next_node

    class LinkedListIterator:
        __current_data = None

        def __init__(self, first_data):
            self.__current_data = first_data

        def __next__(self):
            if self.__current_data is None:
                raise StopIteration
            data = self.__current_data.data
            self.__current_data = self.__current_data.next_node
            return data

    def __init__(self):
        self.__head = None

    def clear(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def __iter__(self):
        return LinkedList.LinkedListIterator(self.__head)

    def add(self, data):
        if self.__head is None:
            self.__head = LinkedList.LinkedListElement(data)

        else:
            current = self.__head
            while current.next_node:
                current = current.next_node
            current.next_node = LinkedList.LinkedListElement(data)

    def insert(self, index, data):
        if self.__head is None:
            self.__head = LinkedList.LinkedListElement(data)
            return

        if index == 0:
            self.__head = LinkedList.LinkedListElement(data, self.__head)
            return

        i = 1
        current = self.__head
        while i != index and current.next_node:
            current = current.next_node
            i += 1
        prev_next = current.next_node
        current.next_node = LinkedList.LinkedListElement(data, prev_next)

    def pop(self, index = 0):
        if self.__head is None:
            return None

        if index == 0:
            element = self.__head
            self.__head = self.__head.next_node
            return element.data

        i = 1
        current = self.__head
        while i != index and current.next_node:
            current = current.next_node
        element = current.next_node
        if element:
            current.next_node = current.next_node.next_node
            return element.data

        return None