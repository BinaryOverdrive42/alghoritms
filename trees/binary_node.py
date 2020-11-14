from typing import Callable, Optional
from queue import Queue


class BinaryNode:
    node_radius = 20
    x_spacing = 20
    y_spacing = 20

    left_child: 'BinaryNode' = None
    right_child: 'BinaryNode' = None
    parent: 'BinaryNode' = None

    def __init__(self, index: int, data: Optional[str] = None):
        self.data = data
        self.index = index

        self.center = (0, 0)
        self.subtree_bounds = (
            self.center[0] - BinaryNode.node_radius,
            self.center[1] - BinaryNode.node_radius,
            self.center[0] + BinaryNode.node_radius,
            self.center[1] + BinaryNode.node_radius,
        )

    def __repr__(self):
        return "BinaryNode(index={})".format(self.index)

    def position_subtree(self, x_min, y_min):
        y_max = y_min + 2 * BinaryNode.node_radius
        x_max = x_min

        if (self.left_child is None) and (self.right_child is None):
            x_max += 2 * BinaryNode.node_radius
            self.subtree_bounds = (x_min, y_min, x_max, y_max)
        else:
            y_max += BinaryNode.y_spacing

            subtree_bottom = y_max

            if self.left_child:
                self.left_child.position_subtree(x_max, y_max)

                x_max = self.left_child.subtree_bounds[2]

                if self.right_child:
                    x_max += BinaryNode.x_spacing

                subtree_bottom = self.left_child.subtree_bounds[3]

            if self.right_child:
                self.right_child.position_subtree(x_max, y_max)

                x_max = self.right_child.subtree_bounds[2]

                if self.right_child.subtree_bounds[3] > subtree_bottom:
                    subtree_bottom = self.right_child.subtree_bounds[3]

            y_max = subtree_bottom
            self.subtree_bounds = (x_min, y_min, x_max, y_max)

        cx = (self.subtree_bounds[0] + self.subtree_bounds[2]) / 2
        cy = y_min + BinaryNode.node_radius
        self.center = (cx, cy)

    def draw_subtree_nodes(self, canvas, bg_color, fg_color):
        x0 = self.center[0] - BinaryNode.node_radius
        y0 = self.center[1] - BinaryNode.node_radius
        x1 = self.center[0] + BinaryNode.node_radius
        y1 = self.center[1] + BinaryNode.node_radius

        canvas.create_oval(x0, y0, x1, y1, fill=bg_color, outline=fg_color)
        canvas.create_text(self.center, text="{}:{}".format(self.index, self.data))

        if self.left_child:
            self.left_child.draw_subtree_nodes(canvas, bg_color, fg_color)
        if self.right_child:
            self.right_child.draw_subtree_nodes(canvas, bg_color, fg_color)

    def draw_subtree_links(self, canvas, color):
        if self.left_child:
            self.left_child.draw_subtree_links(canvas, color)
            canvas.create_line(
                self.center[0],
                self.center[1],
                self.left_child.center[0],
                self.left_child.center[1],
            )
        if self.right_child:
            self.right_child.draw_subtree_links(canvas, color)
            canvas.create_line(
                self.center[0],
                self.center[1],
                self.right_child.center[0],
                self.right_child.center[1]
            )

    def minimum(self):
        if not self.left_child:
            return self
        return self.left_child.minimum()

    def maximum(self):
        if not self.right_child:
            return self
        return self.right_child.maximum()

    def next(self):
        if self.right_child:
            return self.right_child.minimum()
        y = self.parent
        x = self
        while y and x == y.right_child:
            x = y
            y = y.parent
        return y

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
                self.left_child.parent = self
                return self.left_child
            else:
                self.left_child.add_node(index, data)
        else:
            if not self.right_child:
                self.right_child = BinaryNode(index, data)
                self.right_child.parent = self
                return self.right_child
            else:
                self.right_child.add_node(index, data)

    def find_node(self, index: int) -> Optional['BinaryNode']:
        if index == self.index:
            return self

        if index < self.index:
            if self.left_child is None:
                return None
            return self.left_child.find_node(index)
        else:
            if self.right_child is None:
                return None
            return self.right_child.find_node(index)

    def delete_node(self, index: int) -> Optional['BinaryNode']:
        node = self.find_node(index)
        parent = node.parent
        if node is None:
            return None
        else:
            if not node.right_child and not node.left_child:
                if parent.right_child == node:
                    parent.right_child = None
                if parent.left_child == node:
                    parent.left_child = None
            elif not node.right_child or not node.left_child:
                if not node.left_child:
                    if parent.left_child == node:
                        parent.left_child = node.right_child
                    else:
                        parent.right_child = node.right_child
                    node.right_child.parent = parent
                else:
                    if parent.left_child == node:
                        parent.left_child = node.left_child
                    else:
                        parent.right_child = node.left_child
                    node.left_child.parent = parent
            else:
                successor = node.next()
                node.index = successor.index
                node.data = successor.data
                if successor.parent.left_child == successor:
                    successor.parent.left_child = successor.right_child
                    if successor.right_child:
                        successor.right_child.parent = successor.parent
                else:
                    successor.parent.right_child = successor.left_child
                    if successor.left_child:
                        successor.right_child.parent = successor.parent
            return node

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
