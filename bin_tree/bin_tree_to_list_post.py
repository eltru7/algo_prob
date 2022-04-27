def bin_tree_to_list_iterative_1_stack(root):
    # post order => left, right, root
    # iterative traversal using 2 stacks
    nodes_in_order = []
    first_stack = [root]
    second_stack = []

    # push root first, then right , left into stack so when we pop, the order will be left, right, root

    if root is None:
        return

    while first_stack:
        node = first_stack.pop()
        second_stack.append(node)

        if node.left:
            first_stack.append(node.left)

        if node.right:
            first_stack.append(node.right)

    while second_stack:
        new_node = second_stack.pop()
        nodes_in_order.append(new_node)


    return nodes_in_order


def bin_tree_to_list_iterative_2_stacks(root):
    pass