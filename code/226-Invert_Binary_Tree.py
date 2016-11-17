#  Description: 
#  ---------------

#  Invert a binary tree.
#       4
#     /   \
#    2     7
#   / \   / \
#  1   3 6   9
#  to
#       4
#     /   \
#    7     2
#   / \   / \
#  9   6 3   1
#  Trivia:
#  This problem was inspired by this original tweet by Max Howell:
#  Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = []
        if root: queue.append(root)
        while queue:
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            node.left,node.right = node.right,node.left
        return root
        