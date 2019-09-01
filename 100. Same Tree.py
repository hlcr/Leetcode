# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def helper(r1, r2):
            if r1 is None and r2 is not None:
                return False
            elif r1 is not None and r2 is None:
                return False
            elif r1 is None and r2 is None:
                return True
            else:
                if r1.val == r2.val:
                    a = helper(r1.left, r2.left)
                    b = helper(r1.right, r2.right)
                    if a and b:
                        return True
                    else:
                        return False
                else:
                    return False
        return helper(p, q)




