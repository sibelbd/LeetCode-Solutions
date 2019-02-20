"""
Final Result:
Runtime: 100 ms, faster than 91.74% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.4 MB, less than 98.68% of Python3 online submissions for Add Two Numbers.

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        
        # Convert lists to strings, then cast them to int and sum
        
        l1number=""
        l2number=""
        
        while l1 is not None:
            l1number = str(l1.val) + l1number
            l1 = l1.next
        l1number = int(l1number)
        while l2 is not None:
            l2number = str(l2.val) + l2number
            l2 = l2.next
        l2number = int(l2number)
        
        # Total number is the non-reversed string addition of both linked lists
        total_number = str(l1number + l2number)
        
        # convert total number to reversed number final_number
        final_number = ""
        for digit in total_number:
            final_number = digit + final_number
        
        # Set up new linked list
        head = None
        currentNode = None
        nextNode = None
        
        # Add digits of final_number to linked list aka final result
        for digit in final_number:
            nextNode = ListNode(digit)
            if currentNode is not None:
                currentNode.next = nextNode
            currentNode = nextNode
            if head is None:
                head = currentNode

            
        return head
