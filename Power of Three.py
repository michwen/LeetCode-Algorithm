
import math

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n==3**round((math.log(n)/math.log(3)))

if __name__ == "__main__":
    print(Solution().isPowerOfTwo(8))