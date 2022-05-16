"""
给定一个二叉树的root，返回最长的路径的长度 ，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

两个节点之间的路径长度由它们之间的边数表示。

输入：root = [5,4,5,1,1,5]
输出：2
"""
from TreeNode import TreeNode
from TreeNode import CreatTree
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        def digui(node) -> int:
            if node is None:
                return 0
            ans_left = digui(node.left)
            ans_right = digui(node.right)
            if node.left is not None and node.val == node.left.val:
                ans_left += 1
            else:        ##不相等就要归零
                ans_left = 0
            if node.right is not None and node.val == node.right.val:
                ans_right += 1
            else:    ##不相等就要归零
                ans_right = 0
            self.ans = max(self.ans, ans_right + ans_left)
            return max(ans_left, ans_right)
        digui(root)
        return self.ans

if __name__ == '__main__':
    s = [5, 4, 5, 1, 1, 5]
    tree = CreatTree(s)
    s1 = Solution()
    print(s1.longestUnivaluePath(tree))


