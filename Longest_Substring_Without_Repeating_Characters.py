"""
Final Result:
Runtime: 76 ms, faster than 89.80% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.2 MB, less than 5.05% of Python3 online submissions for Longest Substring Without Repeating Characters.

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
Preface: This one was a bit of a doozy to optimize. Runtime is looking good, but I'm having trouble finding ways to optimize the memory usage.
I considered adding a counter to minimize the need to calculate the length of nonrepeating_chars, however this had little to no impact. 
There's probably somewhere I can make one less calculation or use one less variable. Please let me know if you have any ideas!
I'd love to learn how to make this code even more efficient and less resource heavy (and implement it in future projects ;) ).
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # list to hold letters to reference in string
        nonrepeating_chars = ""
        
        #highest counter streak
        highest_streak = 0
        
        # iterate through characters in string
        for char in s:
            
            # condition to check that char hasn't been used prev
            if char not in nonrepeating_chars:
                
                # add char to nonrepeating_ints
                nonrepeating_chars += char
            
            else: 
                
                # streak has been broken
                # if new streak is longer than current highest, update highest streak
                if len(nonrepeating_chars)>=highest_streak:
                    highest_streak = len(nonrepeating_chars)
                
                # add the current char to nonrepeating characters
                nonrepeating_chars += char
                
                # keep only what comes after the first occurance of the repeated char in current streak string
                nonrepeating_chars = nonrepeating_chars[nonrepeating_chars.index(char)+1:]

        # final update to highest streak in case final streak is longest        
        if len(nonrepeating_chars)>highest_streak:
            highest_streak = len(nonrepeating_chars)
        
        return highest_streak
                
