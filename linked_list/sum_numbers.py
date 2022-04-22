class LinkedNode():
    def __init__(self, value):
        self.value = value
        self.next = next


def addTwoNumbers(l1, l2):

    def sum_val(a, b, c):
        ret = 0
        total = a + b + c
        if total >= 10:
            ret = 1
            total = total - 10
        return ret, total

    ret = 0
    res = LinkedNode(0)

    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        ret, total = sum_val(val1, val2, ret)
        res.value = total
        res.next = LinkedNode(0)

        if l1.next:
            l1.next = l1.next.next
            l1.val = l1.next.val

        if l2.next:
            l2.next = l2.next.next
            l2.val = l2.next.val


    return res