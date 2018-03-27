class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None

        previous = head
        current = previous.next

        while current:

            #swap front and back
            next = current.next
            current.next = previous
            previous = current
            current = next

        head.next = None

        return previous


if __name__ == "__main__":

    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    D = ListNode(4)
    E = ListNode(5)
    
    A.next = B
    B.next = C
    C.next = D
    D.next = E

    answer =  Solution().reverseList(A)
    print(answer.val)


