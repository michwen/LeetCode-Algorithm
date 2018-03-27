
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '[%s] -> %s' % (self.val, str(self.next))


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        answer = ListNode(0)
        currentDigit = answer
        while l1 is not None or l2 is not None:
            #addition
            total_val = ((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry)
            val =int(total_val % 10)
            carry = int(total_val / 10)

            #store current val move on
            currentDigit.next = ListNode(val)
            currentDigit = currentDigit.next

            #move on to next digit
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            currentDigit.next = ListNode(carry)
        return answer.next

    def addTwoNodes(self, n1, n2):
        if not n1 and not n2:
            None
        if not n1:
            return n2.val
        if not n2:
            return n1.val
        return n1.val + n2.val


if __name__ == "__main__":
    list = ListNode(2)
    list.next = ListNode(4)
    list.next.next = ListNode(3)


    list2 = ListNode(5)
    list2.next = ListNode(6)
    list2.next.next = ListNode(4)

    print(Solution().addTwoNumbers(list, list2))