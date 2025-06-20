from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i, j in zip(nums, nums[1:]):
            if i % 2 == j % 2:
                return False
        return True


if __name__ == "__main__":
    assert Solution().isArraySpecial([1])
    assert Solution().isArraySpecial([2, 1, 4])
    assert not Solution().isArraySpecial([4, 3, 1, 6])
