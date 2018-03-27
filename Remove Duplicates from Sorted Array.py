class Solution:

    def removeDuplicates(self, nums):
        
        answer = [nums[0]]
        start = 0

        for i in range (len(nums)):
            if(nums[i] !=answer[start]):
                answer.append(nums[i])
                start=start+1

        return answer

if __name__ == "__main__":

    #sorted array
    print(Solution().removeDuplicates([1, 1, 2, 2, 3]))