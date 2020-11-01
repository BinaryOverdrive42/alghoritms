from typing import Callable, Optional
from queue import Queue


class BinaryNode:
    left_child: 'BinaryNode' = None
    right_child: 'BinaryNode' = None

    def __init__(self, index: int, data: Optional[str] = None):
        self.data = data
        self.index = index

    def add_node(self, index: int, data: Optional[str] = None) -> 'BinaryNode':
        """
        Adding a node to build an ordered tree.
        Inorder traversal through such a tree will process values in sorted order
        :param index: int
        :param data: str
        :return: added BinaryNode
        """
        if index < self.index:
            if not self.left_child:
                self.left_child = BinaryNode(index, data)
                return self.left_child
            else:
                self.left_child.add_node(index, data)
        else:
            if not self.right_child:
                self.right_child = BinaryNode(index, data)
                return self.right_child
            else:
                self.right_child.add_node(index, data)

    def traverse_preorder(self, processor: Callable):
        """
        O(N)
        Alert: Can reach maximum recursion depth
        :param processor: Callable
        :return: None
        """
        processor(self)

        if self.left_child:
            self.left_child.traverse_preorder(processor)

        if self.right_child:
            self.right_child.traverse_preorder(processor)

    def traverse_inorder(self, processor: Callable):
        """
        O(N)
        Alert: Can reach maximum recursion depth
        :param processor: Callable
        :return: None
        """
        if self.left_child:
            self.left_child.traverse_inorder(processor)

        processor(self)

        if self.right_child:
            self.right_child.traverse_inorder(processor)

    def traverse_postorder(self, processor: Callable):
        """
        O(N)
        Alert: Can reach maximum recursion depth
        :param processor: Callable
        :return: None
        """
        if self.left_child:
            self.left_child.traverse_postorder(processor)

        if self.right_child:
            self.right_child.traverse_postorder(processor)

        processor(self)

    def traverse_deep_first(self, processor: Callable):
        """
        O(N)
        Recursion is not used, but more memory is required to traverse
        :param processor: Callable
        :return: None
        """
        children: Queue[BinaryNode] = Queue()

        children.put(self)
        while not children.empty():

            node = children.get()

            processor(node)

            if node.left_child:
                children.put(node.left_child)

            if node.right_child:
                children.put(node.right_child)
