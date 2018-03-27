class Solution(object):

    def reverseInteger(self, s):

        st = int(str(s)[::-1])

        return (st)

if __name__ == "__main__":
    print(Solution().reverseInteger(911))