class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        
        #edge case: if n larger than flowerbeds
        if n > len(flowerbed):
            return False
        
        for i in range(len(flowerbed)):

            if flowerbed[i] ==0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    count += 1
                    
        if count >= n:
            return True


        # loop through the flowerbed's length
        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # True
    print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # False