class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        if root is None:
            return

        queue = [root]
        average = []  # [3]
        count = 0
        total = 0

        while queue:  # 3 - 9 - 20
            curr = queue.pop(0)  # queue  [ ]
            count += 1  # count = 2
            total += curr.val  # total =  29

            if len(queue) == 0:

                average.append(total / count)
                count = 0
                total = 0

            if curr.left is not None:
                queue.append(curr.left)

            if curr.right is not None:
                queue.append(curr.right)
        return average
