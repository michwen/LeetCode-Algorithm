class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

if __name__ == "__main__":
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    A.next = B
    B.next = C
    Solution().deleteNode(B)

    print(A.next.val)