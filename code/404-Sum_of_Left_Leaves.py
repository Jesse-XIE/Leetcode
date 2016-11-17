#  Description: 
#  ---------------

#  Find the sum of all left leaves in a given binary tree.
#  Example:
#      3
#     / \
#    9  20
#      /  \
#     15   7
#  
#  There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root] if root else []
        lleaves = [0]
        while queue:
            node = queue.pop(0)
            if node.left: 
                queue.append(node.left)
                if not(node.left.left or node.left.right):
                    lleaves.append(node.left.val)
            if node.right:
                queue.append(node.right)
        return sum(lleaves)
            