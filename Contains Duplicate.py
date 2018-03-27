class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        my_dict = dict([(x,0) for x in nums])
        return (len(nums) > len(my_dict))


    def containsDuplicateSet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))

if __name__ == "__main__":
    print(Solution().containsDuplicate([10,1,1,1,2,0,5]))