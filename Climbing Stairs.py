class Solution(object):

    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2

        ways = [0] * n
        ways[0] = 1
        ways[1] = 2

        for i in range(2, n):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[n - 1]

    def climbStairs2(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2

        return(self.climbStairs(n - 1) + self.climbStairs(n - 2))


if __name__ == "__main__":
    print(Solution().climbStairs(10))