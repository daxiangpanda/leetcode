# 给定一个有 N 个节点的二叉树，每个节点都有一个不同于其他节点且处于 {1, ..., N} 中的值。

# 通过交换节点的左子节点和右子节点，可以翻转该二叉树中的节点。

# 考虑从根节点开始的先序遍历报告的 N 值序列。将这一 N 值序列称为树的行程。

# （回想一下，节点的先序遍历意味着我们报告当前节点的值，然后先序遍历左子节点，再先序遍历右子节点。）

# 我们的目标是翻转最少的树中节点，以便树的行程与给定的行程 voyage 相匹配。 

# 如果可以，则返回翻转的所有节点的值的列表。你可以按任何顺序返回答案。

# 如果不能，则返回列表 [-1]。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        res = []
        i = 0
        def dfs(root):
            # 标志遍历的index
            nonlocal i
            # 如果遍历到的树的根节点为空，那么该子树遍历完毕，满足要求
            if not root:
                return True
            # 如果节点不等于voyage[i]，那么不满足条件,
            if root.val != voyage[i]:
                return False
            # 遍历下一个节点，也就是当前节点的左子树
            i += 1
            # 如果左子树存在，且左子树的值不等，那么交换并记录树根的index
            if root.left and root.left.val != voyage[i]:
                res.append(root.val)
                root.left,root.right = root.right,root.left
            return dft(root.left) and dfs(root.right)
        return res if dfs(root) else [-1]


# 树的内容不太熟悉
