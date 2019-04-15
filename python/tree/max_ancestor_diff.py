# https://leetcode.com/contest/weekly-contest-132/problems/maximum-difference-between-node-and-ancestor/
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def max_diff(node, max_so_far, min_so_far, diff):
            if node is None:
                return diff

            max_so_far = max(max_so_far, node.val)
            min_so_far = min(min_so_far, node.val)
            diff = max_so_far - min_so_far
            
            max_left = max_diff(node.left, max_so_far, min_so_far, diff)
            max_right = max_diff(node.right, max_so_far, min_so_far, diff)

            return max(max_left, max_right)

            
        return max_diff(root, 0, 100000, 0)
