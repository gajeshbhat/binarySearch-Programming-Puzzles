import heapq


class Solution:

    # Time O(n^2*k) Space O(1)
    def solve_naive(self, nums, k):
        for i in range(k):
            min_ele = min(nums)
            min_ele_idx = nums.index(min_ele)
            nums[min_ele_idx] = nums[min_ele_idx] * -1
        return sum(nums)

    # Time O(n*nlogk) Space O(n)
    def solve_nnlogk(self, nums, k):
        pq = []
        for val in nums:
            heapq.heappush(pq, val)
        while k > 0:
            min_value = heapq.heappop(pq)
            heapq.heappush(pq, min_value * -1)
            k -= 1
        return sum(pq)

    # Time O(nlogn) Space O(n)
    def solve_nlogn(self, nums, k):
        sorted_nums = sorted(nums)
        total_sum = 0
        zero = 0

        for index, val in enumerate(sorted_nums):
            if sorted_nums[index] == 0:
                zero = 1
            if sorted_nums[index] < 0 and k > 0:
                sorted_nums[index] = -sorted_nums[index]
                k -= 1
            total_sum += sorted_nums[index]
        if zero == 1 or k == 0 or k % 2 == 0:
            return total_sum
        return total_sum - 2 * min(sorted_nums)
