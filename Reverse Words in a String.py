class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])

if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))
