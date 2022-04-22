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


