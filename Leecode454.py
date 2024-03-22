from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = dict()

        count = 0
        for n1 in nums1:
            for n2 in nums2:
                n12 = n1 + n2
                if n12 in hashmap:
                    hashmap[n12] += 1
                else:
                    hashmap[n12] = 1

        for n3 in nums3:
            for n4 in nums4:
                n34 = n3 + n4
                if -n34 in hashmap:
                    count += hashmap[-n34]

        return count


nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
sol = Solution()
print(sol.fourSumCount(nums1, nums2, nums3, nums4))
