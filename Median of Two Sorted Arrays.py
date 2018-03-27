class Solution:

    def findMedianSortedArrays(self, A, B):
        lenA = len(A)
        lenB = len(B)

        k = (lenA + lenB) // 2

        if (lenA + lenB) % 2 == 0:
            return (self.findKth(A, B, k) + self.findKth(A, B, k + 1))/2

        else:
            return self.findKth(A, B, (lenA + lenB) / 2 + 1)

    def findKth(self, A, B, k):
        lenA=len(A)
        lenB=len(B)

        if (lenA > lenB):
            return self.findKth(B,A,k)

        if (lenA == 0):
            return B[k - 1]
        if (k== 1):
            return min(A[0], B[0])

        #division
        partA = int(min(k / 2,len(A)))
        partB = int(k - partA)

        if (A[partA - 1] < B[partB - 1]):
            return  self.findKth(A[partA:], B, partB);
        elif (A[partA - 1] > B[partB - 1]):
            return  self.findKth(A, B[partB:], partA);

        else:
            return A[partA - 1];


if __name__ == "__main__":

    print(Solution().findMedianSortedArrays([1, 2], [1, 2, 3]))