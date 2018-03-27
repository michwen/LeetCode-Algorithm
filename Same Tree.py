class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    rootA = TreeNode(1)
    rootA.val = "root"
    rootA.left = TreeNode(1)
    rootA.left.val = "left"
    rootA.right = TreeNode(1)
    rootA.right.val = "right"

    rootB = TreeNode(2)
    rootB.val = "root"
    rootB.left = TreeNode(2)
    rootB.left.val = "left"
    rootB.right = TreeNode(2)
    rootB.right.val = "right"

    print(Solution().isSameTree(rootA,rootB))