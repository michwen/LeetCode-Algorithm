
class Solution(object):
    def maxSubarray(self, array):
        max_sum = -1e100
        sum = 0
        for i in range(len(array)):
            sum += array[i]
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                sum = 0
        return max_sum

    def maxProfit(self, prices):

        profit = []
        for i in range(len(prices)-1):
            profit.append(prices[i+1]-prices[i])

        return self.maxSubarray(profit)

if __name__ == "__main__":

    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))