
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


    def __str__(self):
        return '[%s] -> %s' % (self.val, str(self.next))

class Solution(object):

    def mergeTwoLists(self, list1, list2):

        holder = ListNode(-1)
        head = holder

        #always check the next one
        while list1 and list2:
            #always store the small one
            if list1.val >= list2.val:
                holder.next = list2
                list2 = list2.next
            else:
                holder.next = list1
                list1 = list1.next

            holder = holder.next

        #pick up left over
        holder.next = list1 or list2

        #corrected list
        return head.next


    def mergeTwoLists2(self, list1, list2):
        if (list1 is None):
            return list2

        if (list2 is None):
            return list1

        # move the large index until it is good
        if (list1.val > list2.val):
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        # correct order, check next one
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

if __name__ == "__main__":

    A = ListNode(1)
    B = ListNode(8)
    C = ListNode(11)

    D = ListNode(1)
    E = ListNode(3)
    F = ListNode(10)
    G = ListNode(12)

    A.next = B
    B.next = C

    D.next = E
    E.next = F
    F.next = G

    print(Solution().mergeTwoLists(A, D))