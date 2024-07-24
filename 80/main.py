class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        previous_previous_element = nums[0]
        i = 2
        while True:
            if nums[i] == previous_previous_element:
                nums.pop(i)
            else:
                i += 1
                previous_previous_element = nums[i - 2]

            if i == len(nums):
                break

        return i


if __name__ == "__main__":
    s = Solution()

    assert s.remove_duplicates([1, 1, 1, 2, 2, 3]) == 5
    assert s.remove_duplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7
