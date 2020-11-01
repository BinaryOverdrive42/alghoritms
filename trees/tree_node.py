from typing import List


class Branch:
    data: any = None
    child: 'TreeNode'


class TreeNode:
    children: List['Branch'] = []

    def __init__(self, name: str):
        self.name = name
