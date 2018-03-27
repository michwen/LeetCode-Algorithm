class Solution(object):

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        if len(s) <= 1:
            return len(s)

        dict = {}

        start = 0
        longest = 0
        end = 0

        for character in s:

            position = dict.get(character)

            #keep adding
            if position is not None and position >= start:

                length = end - start
                start = position + 1

                longest = max( length, longest)

            dict[character] = end

            #move on
            end=end+1

        return longest

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabdbbbcbbd"))