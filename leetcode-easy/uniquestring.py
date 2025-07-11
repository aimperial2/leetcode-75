class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        occurences = {}
        for char in s:
            if char not in occurences:
                occurences[char] = 1
            else:
                occurences[char] += 1
        for i, char in enumerate(s):
            if occurences[char] == 1:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    string = "leetcode"
    print(s.firstUniqChar(string))  # should print: 0

    string2 = "loveleetcode"
    print(s.firstUniqChar(string2))  # should print: 2
        
    string3 = "aabb"
    print(s.firstUniqChar(string3))  # should print: -1