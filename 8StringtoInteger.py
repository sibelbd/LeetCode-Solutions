# 8. String to Integer (atoi)


# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

# Note:

# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

# Runtime: 36 ms, faster than 92.55% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 14 MB, less than 5.95% of Python3 online submissions for String to Integer (atoi).
# The best way to go about this would have been regex but this solution is without regex. 


class Solution:
    def myAtoi(self, str: str) -> int:
        
        # String to hold int to be returned
        number = ""
        # Boolean whether num is negative
        negative = False
        # nonwhitespace is reached
        whitespace = False
        # single sign found
        sign_specified = False
        # break_loop breaks the loop
        break_loop = False
        
        # read each char in string
        for i in str:
            # needed a break_loop condition to stop processing letters if conditions weren't met
            if break_loop == False:
                # if character is whitespace
                if i == " ":
                    # if numbers haven't been found yet, continue
                    if number == "" and sign_specified == False:
                        continue
                    # if numbers have been found, break loop
                    else:
                        break_loop = True
                # if i is "-"
                elif i == "-":
                    # check if a sign was already declared and no numbers have been recorded
                    if sign_specified == False and number == "":
                        # the sign has been set
                        sign_specified = True
                        # the number is negative
                        negative = True
                    # if numbers have been recorded or sign previously set then break loop
                    else:
                        break_loop = True
                
                elif i == "+":
                    # check if a sign was already declared and no numbers have been recorded
                    if sign_specified == False and number == "":
                        # the sign has been set
                        sign_specified = True
                        continue
                    # if numbers have been recorded or sign previously set then break loop
                    else:
                        break_loop = True
                # if i is a number 0 to 9
                elif i.isdigit():
                    # add char to number
                    number = number + i
                # otherwise break
                else:
                    break
                    
        # return 0 if no number processed
        if number == "":
            return 0 
        # if number is negative
        elif negative == True:
            # if number is larger than 32 bit return min int size
            if (0 - int(number)) < -2**31:
                return -2147483648
            # return negative number    
            else:
                return 0 - int(number)
        #if number is positive
        else:           
            # if number is greater than 32 bits return max int size
            if int(number) > 2**31-1:
                return 2147483647
            # return postive number
            else:
                return int(number)
        
