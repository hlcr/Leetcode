# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False

        def pre_order(root, is_left, r_list):
            if not root:
                if is_left:
                    r_list.append('lnull')
                else:
                    r_list.append('rnull')
                return
            r_list.append('#' + str(root.val))
            pre_order(root.left, True, r_list)
            pre_order(root.right, False, r_list)

        s_list = []
        pre_order(s, False, s_list)
        t_list = []
        pre_order(t, False, t_list)
        ss = "".join(s_list)
        tt = "".join(t_list)
        return tt in ss

