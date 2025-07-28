class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # reverse the order of the string, get rid of the spaces but have the string reversed
        # it will always have atleast ONE word
        # store string into a list without any extra spaces
        reverse_lst = s.split()

        # reverse the string/list by splicing it and return reversed string through join
        return " ".join(reverse_lst[::-1])

if __name__ == "__main__":
    s = Solution()
        
    # Test with some examples: hello world & a good example
    test1 = "  hello   world  "
    result1 = s.reverseWords(test1)
    print(f"Output: '{result1}'")
    
    test2 = "a good   example"
    result2 = s.reverseWords(test2)
    print(f"Output: '{result2}'")

    test3 = "a  rabbit in a tunnel  "
    result3 = s.reverseWords(test3)
    print(f"Output: '{result3}'")
