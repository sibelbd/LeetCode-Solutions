# Runtime: 32 ms, faster than 95.34% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its level order traversal as:
# [
#  [3],
#  [9,20],
#  [15,7]
# ]
#

# This is my first ever binary tree problem. I've done graph and tree theory before for class, but never did any 
# problems until this one. Very happy with the outcome and optimization. 
# I'm proud I was able to optimize it so much on the first try.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # if Node is null return empty array
        if not root:
            return []
        
        # create queue
        queue = [root]
        # create second queue to hold back levels from main queue until level is complete 
        next_level_queue = []
        
        # create level order array (what the final result will be)
        total_level_arr = [[root.val]]
        
        # an array to hold current level of children
        one_level_arr = []
        
        # repeat while queue is not empty (aka nodes still need to be checked)
        while queue:
           
        # add children to next_level_queue if exists
            # and add their values to this level's array
            if queue[0].left != None:
                next_level_queue.append(queue[0].left)
                one_level_arr.append(queue[0].left.val)
            if queue[0].right != None:
                next_level_queue.append(queue[0].right)
                one_level_arr.append(queue[0].right.val)
            
            # remove current node from queue
            del queue[0]
            
            # if the queue is empty, append one_level_arr to total_level_arr and next_level_queue to queue
            if not queue and one_level_arr:
                total_level_arr.append(one_level_arr)
                one_level_arr = []
                queue = next_level_queue
                next_level_queue = []
        
        return total_level_arr
