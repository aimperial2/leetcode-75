class Solution(object):
    def moveZeroes(self, nums):
        # array nums, move all zeros to end, maintaining the order of the nonzeroes
        # no new arrays, no use of .append(), 
        # edge cases:  none array, only zeros, no zeroes within in array
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
                
        return nums

if __name__ == "__main__":
    s = Solution()
    arr = [0, 1, 0, 3, 12]
    s.moveZeroes(arr)
    print(arr)  # should print: [1, 3, 12, 0, 0]

    nums = [0, 0, 1]
    s.moveZeroes(nums)
    print(nums)  # should print: [1, 0, 0]
        
