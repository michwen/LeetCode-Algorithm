class Solution(object):

    def isPalindrome(self, s):

        st = int(str(s)[::-1])

        return (s==st)

if __name__ == "__main__":
    print(Solution().isPalindrome(9110119))