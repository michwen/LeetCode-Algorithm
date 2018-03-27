
class Solution(object):
    def intToRoman(self, num):

        dictionary = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        #dict(map(reversed, dictionary.items()))
        result = ''
        for key in dictionary:
            if(num>=key):
                num=num-key
                result = result+dictionary[key]

        return result

# Test cases
if __name__ == "__main__":
    print(Solution().intToRoman(110))