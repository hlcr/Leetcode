# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class Solution(object):
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.nls = 0
            self.dp = 0

    def helper(self, root):
        if not root:
            return 0
        if root.left:

            self.helper(self.Node(root.left))
        if root.right:
            self.helper(self.Node(root.right))
        exclude_root = 0
        include_root = root.val
        if root.left:
            exclude_root += root.left.dp
            include_root += root.left.nls
            root.nls += root.left.dp

        if root.right:
            exclude_root += root.right.dp
            include_root += root.right.nls
            root.nls += root.right.dp

        root.dp = max(include_root, exclude_root)
        return root.dp




    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(self.Node(root))

if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3

    print(Solution().rob(t1))