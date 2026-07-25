# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for i in range(len(q1)):
                nP = q1.popleft()
                nQ = q2.popleft()

                if nP is None and nQ is None:
                    continue
                if nP is None or nQ is None or nP.val != nQ.val:
                    return False
                
                q1.append(nP.left)
                q1.append(nP.right)
                q2.append(nQ.left)
                q2.append(nQ.right)
        return True