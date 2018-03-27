import math

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n==2**round((math.log(n)/math.log(2)))

if __name__ == "__main__":
    print(Solution().isPowerOfTwo(8))