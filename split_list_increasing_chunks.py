from collections import Counter


class Solution:
    def solve(self, nums, k):
        # Make a dictionary of nums
        nums_dict = Counter(nums)
        # Pick the maximum value in the dictionary
        max_val_dict = max(list(nums_dict.values()))
        # Total sublist needed to accommodate the unique numbers
        if max_val_dict * k <= len(nums):
            return True
        return False
