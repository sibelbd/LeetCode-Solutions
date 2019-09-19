# This is my original, uneditted solution for this problem
# 
# Problem 20: Valid Parenthesis
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Final Totals:
# Runtime: 56 ms, faster than 6.14% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.9 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
# Overall these numbers aren't up to standard for me, but I'm jumping back into algo after 
# an 8 month hiatus with my last internship, so I can't say it's entirely surprising. 
# Now I have a starting point to climb from. One thing I did like with this code is 
# that it's very readable and easy to understand.

class Solution:
    def isValid(self, s: str) -> bool:
        # condition for whether more parenthesis were taken out in the loop or not
        paren_taken_out = True
        
        while paren_taken_out == True:
            # iterate through characters in string
            paren_taken_out = False
            if "[]" in s:
                s = s.replace("[]", "")
                paren_taken_out = True
            
            if "()" in s:
                s = s.replace("()", "")
                paren_taken_out = True
            
            if "{}" in s:
                s = s.replace("{}", "")
                paren_taken_out = True
            
        if paren_taken_out == False:
            if "(" in s or ")" in s or "[" in s or "]" in s or '{' in s or "}" in s:
                return False
            else: 
                return True
            
                
                    
            
