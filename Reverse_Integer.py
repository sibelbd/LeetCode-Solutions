"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose 
of this problem, assume that your function returns 0 when the reversed 
integer overflows."""



class Solution:
    def reverse(self, x: 'int') -> 'int':
        # take the absolute value of int to disregard negative symbols
        string1 = str(abs(x))
        # initialize final reversed int as string for scope
        reversed_int = ""
        
        # if condition for if x was originally negative, add a "-" at the beginning of reversed string
        if x<=0:
            # iterate through chars in string
            for char in string1:
                # add each char to our empty string at the front
                reversed_int = str(char) + reversed_int
            reversed_int = "-" + reversed_int 
        else:
            # iterate through chars in string
            for char in string1:
                #add each char to our empty string at the front
                reversed_int = str(char) + reversed_int
        
        # cast string to int
        reversed_int = int(reversed_int)
        
        # return zero if reversed int is too large for 32-bit signed int
        if abs(reversed_int)<=2**31:
            return reversed_int
        else:
            return 0
