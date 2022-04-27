class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bin_tree_to_list_iterative(root):
    # in order => left, root, right
    # iterative traversal

    nodes_in_order = []
    stack = []
    current = root

    while True:
        if current is not None:
            stack.append(current)
            current = current.left

        elif stack:
            current = stack.pop()
            nodes_in_order.append(current)
            current = current.right

        else:
            break

    return nodes_in_order