#3. Longest Substring Without Repeating Characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#using sliding window technic
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        charSet = set()
        left = 0

        for right in range(len(s)):
            while s[right] in charSet():
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, right-left+1)
            
        return result

#time - O(n)
#space - O(n)