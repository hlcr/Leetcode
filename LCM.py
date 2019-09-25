class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root, val):
    if root == None:
        root = Node(val)
    elif root.val > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def pre_order(root):
    if not root:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


def distance_from_root(root, x):
    if not root:
        return -1
    if root.val == x:
        return 0
    elif root.val < x:
        if distance_from_root(root.right, x) != -1:
            return 1+distance_from_root(root.right, x)
        else:
            return -1
    else:
        if distance_from_root(root.left, x) != -1:
            return 1+distance_from_root(root.left, x)
        else:
            return -1


def distanceBetween2(root, a, b):
    if root.val < a and root.val < b:
        return distanceBetween2(root.right, a, b)
    elif root.val > a and root.val > b:
        return distanceBetween2(root.left, a, b)
    else:
        da = distance_from_root(root, a)
        db = distance_from_root(root, b)
        if da != -1 and db != -1:
            return da+db
        else:
            return -1

if __name__ == '__main__':
    root = None
    root = insert(root, 20)
    insert(root, 10)
    insert(root, 5)
    insert(root, 15)
    insert(root, 30)
    insert(root, 25)
    insert(root, 35)

    # pre_order(root)
    print(distanceBetween2(root, 45, 0))
