class Queue:
    def __init__(self):
        self.__queue = []

    def is_empty(self):
        return not self.__queue

    def push(self, element):
        self.__queue.append(element)

    def pop(self):
        if self.is_empty():
            return None

        result = self.__queue.pop()
        return result


    def size(self):
        return len(self.__queue)

    def clear(self):
        self.__queue = []