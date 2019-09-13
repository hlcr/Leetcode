# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #     def compare(self, a, b):
    #         if not a and not b:
    #             return True

    #         if (a and not b) or (not a and b) or (a.val != b.val):
    #             return False

    #         return self.compare(a.left, b.left) and self.compare(a.right, b.right)

    #     def helper(self, s, value):
    #         if not s:
    #             return
    #         if s.val == value:
    #             self.r_list.append(s)
    #         ls =  self.helper(s.left, value)
    #         rs = self.helper(s.right, value)

    #     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    #         if not s or not t:
    #             return False
    #         self.r_list = []
    #         self.helper(s, t.val)

    #         if not self.r_list:
    #             return False
    #         for k in self.r_list:
    #             if self.compare(k, t):
    #                 return True
    #         return False
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

