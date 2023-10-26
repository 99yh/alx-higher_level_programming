#!/usr/bin/python3
"""Make a linked list."""


class SinglyLinkedList:
    """Make an empty one."""

    def __init__(self):
        """Initialize empty one."""
        self.__head = None

    def sorted_insert(self, value):
        """Add node in a sorted order"""
        new_node = Node(value)
        prev = None
        next = self.__head
        while next is not None and next.data < new_node.data:
            prev = next
            next = next.next_node

        new_node.next_node = next
        if prev is None:
            self.__head = new_node
        else:
            prev.next_node = new_node

    def __str__(self):
        """Act as a string"""
        move = self.__head
        ret = ""
        while move is not None:
            ret += str(move.data) + '\n'
            move = move.next_node
        return ret[:-1]


class Node:
    """Make new Node inestence"""

    def __init__(self, data, next_node=None):
        """Make new Node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data."""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node."""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
