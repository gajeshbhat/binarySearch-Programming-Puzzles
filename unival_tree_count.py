# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Conditions for Univalue
1. If a Node is leaf - Univalue
2. If Node is a parent -> left,right and parent node same value - Univalue
3. If a Node only has left or right child and the children are leaves then if the value of that child and parent match - Univalue
"""


class Solution:
    def get_univalue(self, root, uni_val_count):
        # If Empty tree return 0
        if root == None:
            return
        elif root.left == None and root.right == None:
            # Leaf node : Count 1 Univalue
            uni_val_count[0] += 1
            return True
        # Check for subtrees
        is_sub_tree_unival = True  # Because Subtree with single child of same value is considered univalue node
        if root.left != None:
            is_sub_tree_unival = self.get_univalue(root.left,
                                                   uni_val_count) and is_sub_tree_unival and root.left.val == root.val  # If left subtree has the same value till end. If even one node has different value then subtree is not univalue. Hence "and" check on left, right and current node value
        if root.right != None:
            is_sub_tree_unival = self.get_univalue(root.right,
                                                   uni_val_count) and is_sub_tree_unival and root.right.val == root.val  # If right subtree has the same value till end. If even one node has different value then subtree is not univalue. Hence "and" check on left, right and current node value

        # Last Non-leaf level stub check
        if is_sub_tree_unival:
            uni_val_count[0] += 1
            return True
        else:
            return False

    def solve(self, root):
        uni_val_count = [0]
        self.get_univalue(root, uni_val_count)
        return uni_val_count[0]
