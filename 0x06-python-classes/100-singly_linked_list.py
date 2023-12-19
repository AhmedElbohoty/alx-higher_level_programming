#!/usr/bin/python3
""" Defines SinglyLinkedList and Node classes

    SinglyLinkedList: to create a singly linked list
    Node: to create node of a singly linked list
"""


#!/usr/bin/python3
class Node:
    """ create node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """ Init a node of a singly linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get node data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ Add new node

            Args:
                value (int): the new node data
            
            Raises:
                TypeError: data must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Get next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Update next node

            Args:
                value (int): the new node data
            
            Raises:
                TypeError: next_node must be a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Create a singly linked list
    """

    def __init__(self):
        """Init a singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new Node into the correct sorted
            position in the list (increasing order)

            Args:
                value (int): new value
        """
        new_node = Node(value)


    def __str__(self):
        res = ""
        node = self.__head
        while node:
            res += str(node.data) + '\n'
            node = node.next_node

        return res[: -1]
