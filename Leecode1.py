from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for index, value in enumerate(nums):
            if target - value in records:
                return [records[target - value], index]
            records[value] = index
        return []


nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))
