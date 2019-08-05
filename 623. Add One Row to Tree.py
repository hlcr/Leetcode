# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root:
            return root
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        queue = [(root, 1)]
        pq = []
        while queue:
            node, level = queue.pop(0)
            if level == d:
                break
            if level == d - 1:
                ln = TreeNode(v)
                rn = TreeNode(v)
                ln.left, node.left = node.left, ln
                rn.right, node.right = node.right, rn
            else:
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
        return root
