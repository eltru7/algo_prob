import math

def verify(node, lower_limit, higher_limit):
    if node is None:
        return True
    if node.val <= lower_limit or  node.val >= higher_limit:
        return False
    return verify(node.left, lower_limit, node.val) and verify(node.right, node.val, higher_limit)

def is_valid_bst_recursive(self, root):
    return self.verify(root, -math.inf, math.inf)
