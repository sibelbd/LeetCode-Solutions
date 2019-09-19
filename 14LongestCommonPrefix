# This is my orginal solution for this problem 
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Runtime: 40 ms, faster than 72.13% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.7 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.
 
 def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        prefix_index = 1
        
        # if array is only one word, return that one word
        if len(strs) == 1:
            return strs[0]
        # if array has more than one word
        # because it isn't empty or length of one
        elif len(strs) != 0:
            # set a test word
            test_word = strs[0]

            # loop as many times as there are letters in the test word
            for letter in test_word:
                for word in strs[1:]:
                    if word[:prefix_index] != test_word[:prefix_index]:
                        return longest_prefix
                longest_prefix = test_word[:prefix_index]
                prefix_index = prefix_index + 1
        return longest_prefix
                
