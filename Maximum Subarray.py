class Solution(object):
    def maxSubArray(self, nums):

        # starting sum
        maxiumSum = runningSum = nums[0]

        # starting index
        i = begin = end = 0

        # keep updating runningSum
        for j in range(1, len(nums)):
            # adjust starting index if the previous sum smaller
            if nums[j] > (runningSum + nums[j]):
                runningSum = nums[j]
                i = j
            # if the previous sum add up larger keep i, starting index
            else:
                runningSum = runningSum + nums[j]

            # the two cases updated the maxiumSum and starting and ending indexes if the current runningSum>maxiumSum
            if runningSum > maxiumSum:
                maxiumSum = runningSum
                begin = i
                end = j

        return nums[begin:end], maxiumSum


if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))