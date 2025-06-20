class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        result = []

        for n in range(len(candies)):
            if candies[n] + extraCandies >= max_candies:
                result.append(True)
            else: 
                result.append(False)

        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.kidsWithCandies([2,3,5,1,3], 3))  #[true,true,true,false,true]
    print(sol.kidsWithCandies([4,2,1,1,2], 2))  #[true,true,false,false,true]