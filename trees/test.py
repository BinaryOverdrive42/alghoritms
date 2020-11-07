import tkinter as tk
from binary_node import BinaryNode


class AppWindow:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self, root_node: BinaryNode):
        self.window = tk.Tk()
        self.window.title("Tree")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)

        canvas = tk.Canvas(
            self.window,
            bg="white",
            borderwidth=2,
            relief=tk.SUNKEN,
        )
        canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        root_node.position_subtree(10, 10)

        root_node.draw_subtree_links(canvas, "black")
        root_node.draw_subtree_nodes(canvas, "white", "blue")

        self.window.focus_force()
        self.window.mainloop()


def create_test_tree():
    root_node = BinaryNode(data="D", index=4)
    b_node = BinaryNode(data="B", index=2)
    e_node = BinaryNode(data="E", index=5)
    a_node = BinaryNode(data="A", index=1)
    c_node = BinaryNode(data="C", index=3)

    root_node.left_child = b_node
    root_node.right_child = e_node

    b_node.left_child = a_node
    b_node.right_child = c_node

    return root_node


def test_traverse_preorder(root_node: BinaryNode):
    values = []
    root_node.traverse_preorder(processor=lambda x: values.append(x.data))
    print(values)

    assert values == ['D', 'B', 'A', 'C', 'E']


def test_traverse_inorder(root_node: BinaryNode):
    values = []
    root_node.traverse_inorder(processor=lambda x: values.append(x.data))
    print(values)

    assert values == ['A', 'B', 'C', 'D', 'E']


def test_traverse_postorder(root_node: BinaryNode):
    values = []
    root_node.traverse_postorder(processor=lambda x: values.append(x.data))
    print(values)

    assert values == ['A', 'C', 'B', 'E', 'D']


def test_traverse_deep_first(root_node: BinaryNode):
    values = []
    root_node.traverse_deep_first(processor=lambda x: values.append(x.data))
    print(values)

    assert values == ['D', 'B', 'E', 'A', 'C']


def test_add_node(root_node: BinaryNode):
    values = []
    items = [
        {
            "index": 7,
            "data": 'G'
        },
        {
            "index": 8,
            "data": "last"
        },
        {
            "index": 6,
            "data": "F"
        }
    ]
    for item in items:
        root_node.add_node(**item)

    root_node.traverse_inorder(processor=lambda x: values.append({
        "index": x.index,
        "name": x.data
    }))

    print(values)


def test_find_node(root_node: BinaryNode):
    node_ = root_node.find_node(7)
    assert node_ is not None
    assert node_.index == 7


if __name__ == "__main__":
    root = create_test_tree()
    test_traverse_preorder(root)
    test_traverse_inorder(root)
    test_traverse_postorder(root)
    test_traverse_deep_first(root)
    test_add_node(root)
    test_find_node(root)

    root_node = BinaryNode(data="A", index=1)
    root_node.add_node(data="B", index=4)
    root_node.add_node(data="C", index=3)
    root_node.add_node(data="D", index=2)
    root_node.traverse_inorder(
        processor=lambda x: print(x.index)
    )
    print(root_node.find_node(index=3))
    AppWindow(root_node)

