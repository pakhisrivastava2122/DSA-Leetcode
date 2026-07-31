"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        def postorderTraversal(node):
            if node is None :
                return 
            
            for child in node.children:
                postorderTraversal(child)

            result.append(node.val)

        postorderTraversal(root)
        return result 
