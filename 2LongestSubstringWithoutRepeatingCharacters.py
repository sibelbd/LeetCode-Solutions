# Runtime: 48 ms, faster than 94.30% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.3 MB, less than 51.87% of Python3 online submissions for Longest Substring Without Repeating Characters.
# https://leetcode.com/submissions/detail/424778428/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        substr = ''
        curr_substr_count = 0
        
        for character in s:
            
            if character not in substr:
                curr_substr_count += 1
                substr += character
            else:
                substr += character
                substr = substr[substr.index(character) + 1:]
                curr_substr_count = len(substr)
            
            if curr_substr_count > longest_substring:
                longest_substring = curr_substr_count
                
            
        return longest_substring
