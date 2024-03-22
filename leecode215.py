import queue
import heapq
import typing


class Solution:
    def findKthLargest(self, nums, k) -> int:
        return heapq.nlargest(k, nums, int.__lt__)[0]


sol = Solution()
sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
