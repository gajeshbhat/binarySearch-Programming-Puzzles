# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def calc_sum(self, root, sum_val):
        if root == None:
            return
        else:
            sum_val[0] += root.val
            if root.left:
                self.calc_sum(root.left, sum_val)
            if root.right:
                self.calc_sum(root.right, sum_val)

    def solve(self, root):
        sum_val_arr = [0]
        self.calc_sum(root, sum_val_arr)
        return sum_val_arr[0]
