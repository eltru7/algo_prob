class LinkedNode():
    def __init__(self, value, next):
        self.value = value
        self.next = next


class MyLinkedList(object):
    def __init__(self):
        self.head = LinkedNode(None, None)

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.head
        for i in range(index):
            if curr:
                curr = curr.next
        return curr.value if curr is not None else None

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_head = LinkedNode(val, self.head)
        self.head = new_head

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        tail = self.head
        next_node = self.head.next
        while next_node:
            next_node = next_node.next
        tail.next = LinkedNode(val, None)


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # what if index is out of range, do we add the node to the tail?

        if index == 0:
            self.addAtHead(val)
        else:
            previous_node = self.head
            for i in range(index - 1):
                if previous_node:
                    previous_node = previous_node.next

            current_node = self.head
            for i in range(index):
                if current_node.next:
                    current_node = current_node.next

            new_node = LinkedNode(val, current_node)
            if previous_node:
                previous_node.next = new_node

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index == 0:
            self.head = LinkedNode(None, None)

        previous_node = self.head
        next_node = self.head

        for i in range(index - 1):
            if previous_node:
                previous_node = previous_node.next

        for i in range(index + 1):
            if next_node:
                next_node = next_node.next

        if previous_node:
            previous_node.next = next_node
