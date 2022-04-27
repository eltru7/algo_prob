class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def _flatten_child(node):
    if node:
        if node.left:
            node.left.right = node.left

        node.right = node.left
        node.left = None

        _flatten_child(node.left)
        _flatten_child(node.right)

def flatten(root):
    """
    recursive way
    pre-order = root, left, right

          4
        /    \
        2    6            4 - 2 - 6

    """
    _flatten_child(root.left)
    _flatten_child(root.right)



class Solution(object):
    def pre_order(self, root):
        """
        pre order traversal, root, left, right
        """
        bin_tree = []
        stack = []
        if root is not None:
            stack.append(root)

        while stack:
            root = stack.pop()
            if root is not None:
                bin_tree.append(root.val)
                stack.append(root.right)
                stack.append(root.left)

        return bin_tree

    # TODO verif


