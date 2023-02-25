from Structure.Linked_List import LinkedList
from Structure.Queue import Queue

class Personal:

    def __init__(self, last_name, position):
        self.__last_name = last_name
        self.__position = position

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, data):
        self.__last_name = data

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, data):
        self.__position = data

class Development(LinkedList):

    def __init__(self, development_number):
        super().__init__()
        self.__development_number = development_number

    @property
    def development_number(self):
        return self.__development_number

    @development_number.setter
    def development_number(self, data):
        self.__development_number = data

class Bank(Queue):

    def __init__(self, bank_name):
        super().__init__()
        self.__bank_name = bank_name

    @property
    def bank_name(self):
        return self.__bank_name

    @bank_name.setter
    def bank_name(self, data):
        self.__bank_name = data