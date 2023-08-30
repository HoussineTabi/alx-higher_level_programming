#!/usr/bin/python3
"""
Singly linked list with python
"""


class Node:
    """
    class Node that defines a node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        This method is used to initialize a node
        """
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")
        if isinstance(data, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """
        return the linked list
        """
        return self.data

    @data.setter
    def data(self, value):
        """
        sets a new value into the self.data
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def nex_node(self):
        """
        retrieve the data from the private attribute self.next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        sets a new value in the next_node
        """
        if isinstance(value, Node):
            value.__next_node = self.__next_node
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    class SinglyLinkedList that defines a singly linked list
    """


    def __init__(self):
        """
        initialize a linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert an element at the head
        """
        if isinstance(value, Node):
            value.__next_node = self.__head
            self.__head = value
            return value
        return None
    def __str__(self):
        strl = ""
        head = self.__head
        while head != None:
            strl += str(head.__data) + '\n'
            head = head.__next_node
        return strl
sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)

