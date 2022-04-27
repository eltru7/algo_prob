class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bin_tree_to_list_iterative(root):
    # pre order => root, left, right
    # iterative traversal

    nodes_in_order = []
    stack = [root]

    if root is None:
        return

    while stack:
        node = stack.pop()

        nodes_in_order.append(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)



    return nodes_in_order