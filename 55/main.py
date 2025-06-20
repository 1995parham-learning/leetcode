def can_jump(nums: list[int]) -> bool:
    queue: list[int] = []
    seen: set[int] = set()

    if len(nums) == 1:
        return True

    queue.append(0)
    seen.add(0)

    while len(queue) != 0:
        index = queue.pop(0)

        for i in range(index + 1, min(index + 1 + nums[index], len(nums))):
            if i not in seen:
                seen.add(i)
                if i == len(nums) - 1:
                    return True
                queue.append(i)

    return False


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4])
    assert not can_jump([3, 2, 1, 0, 4])
