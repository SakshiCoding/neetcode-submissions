# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        stack = [(root, False)]
        heights = {None: 0}
        diameter = 0

        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if visited:
                left = heights[node.left]
                right = heights[node.right]

                heights[node] = 1 + max(left, right)
                diameter = max(diameter, left + right)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return diameter